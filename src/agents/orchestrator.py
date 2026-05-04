from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable

from src.config import get_llm

VALID_INTENTS = {"HR", "TECH", "FINANCE"}

_SYSTEM = """Eres el clasificador de intención de un sistema de soporte empresarial.
Tu única tarea es determinar el departamento al que pertenece la consulta del usuario.

Responde ÚNICAMENTE con una de estas etiquetas (sin explicación ni puntuación):
- HR       → Recursos Humanos: vacaciones, licencias, beneficios médicos, código de conducta, evaluaciones de desempeño, onboarding, capacitación, políticas de trabajo (remoto/híbrido), bandas salariales y políticas de compensación.
- TECH     → Soporte de IT: contraseñas, VPN, accesos a sistemas, software, hardware, laptops, malware, incidentes de seguridad, GitHub, impresoras, red corporativa, cloud (AWS/GCP).
- FINANCE  → Finanzas: gastos y reembolsos, facturas, tarjeta corporativa, pagos a proveedores, presupuestos, impuestos, tesorería, y todo lo relacionado con NÓMINA (cuándo se paga, montos, deducciones, recibos, anticipos, datos bancarios, retenciones).
- UNKNOWN  → Si la consulta no pertenece claramente a ninguno de los anteriores.

Reglas de desambiguación importantes:
1. Las consultas sobre **NÓMINA** (cuándo cobro, recibo de sueldo, deducciones, datos bancarios, anticipo de salario, retenciones de impuestos, fechas de pago, montos) → **FINANCE**, no HR.
2. Las consultas sobre **políticas de compensación** (bandas salariales, estructura de bonos, equity, revisiones de mérito) → **HR**.
3. Las consultas sobre **acceso a sistemas** (incluso si el sistema es de RRHH o Finanzas) → **TECH**.
4. Las consultas sobre **comprar/instalar software** → **TECH**, aunque pregunten quién paga.

Ejemplos:
Consulta: "¿Cuándo me depositan el sueldo este mes?"
Respuesta: FINANCE

Consulta: "Necesito ver mi recibo de nómina con las deducciones del mes"
Respuesta: FINANCE

Consulta: "¿Cuál es la banda salarial para mi nivel?"
Respuesta: HR

Consulta: "Quiero solicitar un anticipo de mi quincena"
Respuesta: FINANCE

Consulta: "No puedo entrar al portal de empleados, me marca contraseña incorrecta"
Respuesta: TECH

Consulta: "¿Cuántos días de vacaciones tengo?"
Respuesta: HR

Ahora clasifica esta consulta:
{query}"""

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
