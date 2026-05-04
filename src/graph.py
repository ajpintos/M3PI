from typing import TypedDict

from langgraph.graph import END, StateGraph

from src.agents.orchestrator import build_orchestrator, classify_intent
from src.agents.rag_agent import build_rag_agent

# Pre-construir los RAG agents (se reusan entre invocaciones)
_rag_agents = {
    "hr": build_rag_agent("hr"),
    "tech": build_rag_agent("tech"),
    "finance": build_rag_agent("finance"),
}
_orchestrator = build_orchestrator()


class State(TypedDict):
    query: str
    intent: str
    answer: str
    domain_used: str


# ── Nodos ──────────────────────────────────────────────────────────────────────

def classify_node(state: State) -> State:
    intent = classify_intent(state["query"], chain=_orchestrator)
    return {**state, "intent": intent}


def _rag_node(domain: str, state: State) -> State:
    answer = _rag_agents[domain].invoke(state["query"])
    return {**state, "answer": answer, "domain_used": domain}


def hr_node(state: State) -> State:
    return _rag_node("hr", state)


def tech_node(state: State) -> State:
    return _rag_node("tech", state)


def finance_node(state: State) -> State:
    return _rag_node("finance", state)


def fallback_node(state: State) -> State:
    answer = (
        "Lo siento, no pude determinar a qué departamento pertenece tu consulta. "
        "Por favor, contacta directamente al área correspondiente: "
        "RRHH (hr@empresa.com), IT Support (it@empresa.com) o Finanzas (finance@empresa.com)."
    )
    return {**state, "answer": answer, "domain_used": "fallback"}


# ── Conditional edge ──────────────────────────────────────────────────────────

def route(state: State) -> str:
    intent = state.get("intent", "UNKNOWN").upper()
    mapping = {"HR": "hr", "TECH": "tech", "FINANCE": "finance"}
    return mapping.get(intent, "fallback")


# ── Construcción del grafo ─────────────────────────────────────────────────────

def build_graph():
    graph = StateGraph(State)

    graph.add_node("classify", classify_node)
    graph.add_node("hr", hr_node)
    graph.add_node("tech", tech_node)
    graph.add_node("finance", finance_node)
    graph.add_node("fallback", fallback_node)

    graph.set_entry_point("classify")

    graph.add_conditional_edges(
        "classify",
        route,
        {
            "hr": "hr",
            "tech": "tech",
            "finance": "finance",
            "fallback": "fallback",
        },
    )

    for node in ["hr", "tech", "finance", "fallback"]:
        graph.add_edge(node, END)

    return graph.compile()


app = build_graph()
