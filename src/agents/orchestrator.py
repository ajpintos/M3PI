from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable

from src.config import get_llm

VALID_INTENTS = {"HR", "TECH", "FINANCE"}

_SYSTEM = """Eres el clasificador de intención de un sistema de soporte empresarial.
Tu única tarea es determinar el departamento al que pertenece la consulta del usuario.

Responde ÚNICAMENTE con una de estas etiquetas (sin explicación ni puntuación adicional):
- HR       → Recursos Humanos: vacaciones, licencias, beneficios, nómina, código de conducta, evaluaciones, incorporación, capacitación.
- TECH     → Soporte de IT: contraseñas, VPN, accesos, software, hardware, incidentes de seguridad, GitHub, impresoras, red, cloud.
- FINANCE  → Finanzas: gastos, reembolsos, facturas, presupuestos, tarjeta corporativa, pagos a proveedores, tesorería, impuestos.
- UNKNOWN  → Si la consulta no pertenece claramente a ninguno de los anteriores.

Consulta del usuario: {query}"""

_prompt = ChatPromptTemplate.from_messages([("human", _SYSTEM)])


def build_orchestrator() -> Runnable:
    return _prompt | get_llm() | StrOutputParser()


def classify_intent(query: str, chain: Runnable | None = None) -> str:
    """Devuelve la etiqueta de intención normalizada."""
    if chain is None:
        chain = build_orchestrator()

    raw: str = chain.invoke({"query": query}).strip().upper()

    # Normalizar en caso de que el modelo devuelva texto extra
    for intent in VALID_INTENTS:
        if intent in raw:
            return intent
    return "UNKNOWN"
