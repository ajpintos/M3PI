from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnablePassthrough

from src.config import get_llm
from src.vector_store import get_retriever

_PERSONAS: dict[str, str] = {
    "hr": (
        "Eres el Agente de Recursos Humanos de la empresa. "
        "Respondes consultas sobre vacaciones, licencias, beneficios, nómina, "
        "evaluaciones de desempeño, código de conducta y política de RRHH."
    ),
    "tech": (
        "Eres el Agente de Soporte Técnico (IT) de la empresa. "
        "Respondes consultas sobre VPN, contraseñas, accesos, software, hardware, "
        "seguridad de endpoints, GitHub, red corporativa y servicios cloud."
    ),
    "finance": (
        "Eres el Agente de Finanzas de la empresa. "
        "Respondes consultas sobre gastos, reembolsos, tarjeta corporativa, facturas, "
        "presupuestos, pagos a proveedores, nómina y cumplimiento fiscal."
    ),
}

_TEMPLATE = """{persona}

Responde la pregunta del usuario basándote ÚNICAMENTE en el siguiente contexto de la documentación interna de la empresa.
Si la información no está en el contexto, indícalo claramente y sugiere contactar al equipo correspondiente directamente.
No inventes información ni salgas del contexto provisto.

Contexto:
{context}

Pregunta: {question}

Respuesta:"""


def _format_docs(docs) -> str:
    return "\n\n".join(doc.page_content for doc in docs)


def build_rag_agent(domain: str, k: int = 4) -> Runnable:
    """Construye y devuelve el RAG chain para el dominio especificado."""
    persona = _PERSONAS[domain]
    retriever = get_retriever(domain, k=k)

    prompt = ChatPromptTemplate.from_template(_TEMPLATE)

    chain = (
        {
            "context": retriever | _format_docs,
            "question": RunnablePassthrough(),
            "persona": lambda _: persona,
        }
        | prompt
        | get_llm()
        | StrOutputParser()
    )
    return chain
