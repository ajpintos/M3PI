"""
CLI principal del sistema multi-agente.

Uso:
  python -m src.main "¿Cuántos días de vacaciones tengo?"
  python -m src.main --batch test_queries.json
"""

import argparse
import json
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from src.graph import app
from src.agents.evaluator import evaluate_response
from src.observability import build_callback, get_langfuse_client, new_session_id


def run_query(query: str, session_id: str, evaluate: bool = True) -> dict:
    callback = build_callback()
    langfuse = get_langfuse_client()

    # En Langfuse v3 envolvemos la invocación en un span para obtener trace_id
    # y enriquecer el trace con metadata útil (session, tags, query original).
    with langfuse.start_as_current_span(
        name="multi-agent-routing",
        input={"query": query},
    ) as span:
        result: dict = app.invoke(
            {"query": query, "intent": "", "answer": "", "domain_used": ""},
            config={"callbacks": [callback]},
        )

        span.update_trace(
            session_id=session_id,
            tags=["routing", result.get("intent", "unknown").lower()],
            metadata={
                "query": query,
                "intent": result.get("intent"),
                "domain_used": result.get("domain_used"),
            },
            output={"answer": result.get("answer"), "intent": result.get("intent")},
        )

        trace_id = span.trace_id

    if evaluate and trace_id:
        try:
            evaluate_response(
                query=result["query"],
                answer=result["answer"],
                trace_id=trace_id,
            )
        except Exception as exc:
            print(f"  [evaluator] Error al evaluar: {exc}", file=sys.stderr)

    langfuse.flush()
    return result


def run_batch(queries_path: Path) -> None:
    with queries_path.open(encoding="utf-8") as f:
        test_cases = json.load(f)

    total = len(test_cases)
    correct = 0
    session_id = new_session_id()

    print(f"\n{'─'*60}")
    print(f"{'QUERY':<45} {'ESPERADO':<10} {'OBTENIDO':<10} OK")
    print(f"{'─'*60}")

    for case in test_cases:
        query = case["query"]
        expected = case.get("expected_intent", "?").upper()

        result = run_query(query, session_id, evaluate=True)
        obtained = result["intent"].upper()

        match = "OK" if obtained == expected else "X"
        if obtained == expected:
            correct += 1

        short_query = query[:43] + ".." if len(query) > 45 else query
        print(f"{short_query:<45} {expected:<10} {obtained:<10} {match}")

    accuracy = correct / total * 100 if total > 0 else 0
    print(f"{'─'*60}")
    print(f"Accuracy de routing: {correct}/{total} ({accuracy:.1f}%)\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Sistema multi-agente de routing")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("query", nargs="?", help="Consulta a procesar")
    group.add_argument("--batch", metavar="FILE", help="JSON con queries de prueba")
    parser.add_argument("--no-eval", action="store_true", help="Desactivar evaluador Langfuse")

    args = parser.parse_args()

    if args.batch:
        batch_path = Path(args.batch)
        if not batch_path.exists():
            print(f"Error: no se encontró el archivo '{batch_path}'", file=sys.stderr)
            sys.exit(1)
        run_batch(batch_path)
    else:
        session_id = new_session_id()
        result = run_query(args.query, session_id, evaluate=not args.no_eval)

        print(f"\n{'─'*60}")
        print(f"  Intención detectada : {result['intent']}")
        print(f"  Agente utilizado    : {result['domain_used']}")
        print(f"{'─'*60}")
        print(f"\n{result['answer']}\n")


if __name__ == "__main__":
    main()
