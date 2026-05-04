"""
Agente Evaluador (BONUS)

Usa un LLM como juez (LLM-as-judge) para puntuar cada respuesta RAG en tres dimensiones:
  - relevance   : ¿La respuesta es relevante a la pregunta?
  - completeness: ¿La respuesta cubre todos los aspectos importantes de la pregunta?
  - accuracy    : ¿La información proporcionada es precisa y no inventa datos?

Los scores (1-10) se envían a Langfuse mediante la Score API de v3 y quedan asociados al trace.
"""

import json

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langfuse import get_client

from src.config import get_llm

_JUDGE_TEMPLATE = """Eres un evaluador experto de respuestas de sistemas de soporte empresarial.

Evalúa la siguiente respuesta en tres dimensiones y devuelve ÚNICAMENTE un JSON válido con esta estructura:
{{"relevance": <1-10>, "completeness": <1-10>, "accuracy": <1-10>}}

Criterios de puntuación:
- relevance (1-10): ¿La respuesta aborda directamente la pregunta? 10=perfectamente relevante, 1=completamente irrelevante.
- completeness (1-10): ¿La respuesta cubre todos los aspectos importantes de la pregunta? 10=completa, 1=incompleta.
- accuracy (1-10): ¿La información es precisa, sin contradicciones ni datos inventados? 10=totalmente precisa, 1=incorrecta.

Pregunta del usuario:
{query}

Respuesta del sistema:
{answer}

JSON de evaluación:"""

_prompt = ChatPromptTemplate.from_template(_JUDGE_TEMPLATE)


def compute_scores(query: str, answer: str) -> dict[str, float]:
    """Llama al LLM-as-judge y devuelve los scores SIN registrarlos."""
    chain = _prompt | get_llm() | StrOutputParser()

    raw = chain.invoke({"query": query, "answer": answer}).strip()

    # Extraer el JSON aunque el modelo devuelva texto adicional
    start = raw.find("{")
    end = raw.rfind("}") + 1
    scores_raw = json.loads(raw[start:end])

    scores = {
        "relevance": float(scores_raw.get("relevance", 5)),
        "completeness": float(scores_raw.get("completeness", 5)),
        "accuracy": float(scores_raw.get("accuracy", 5)),
    }
    scores["overall"] = round(sum(scores.values()) / 3, 2)
    return scores


def register_scores(scores: dict[str, float]) -> None:
    """Registra los scores en el span/trace activo de Langfuse v3.
    Debe llamarse DENTRO del contexto de un @observe o start_as_current_observation."""
    langfuse = get_client()
    for name, value in scores.items():
        # Probamos los métodos disponibles en distintas variantes de v3
        for method_name in ("score_current_span", "score_current_trace", "score"):
            method = getattr(langfuse, method_name, None)
            if callable(method):
                try:
                    method(
                        name=name,
                        value=value,
                        data_type="NUMERIC",
                        comment=f"LLM-as-judge score for '{name}'",
                    )
                    break
                except Exception:
                    continue


def evaluate_response(query: str, answer: str, trace_id: str | None = None) -> dict[str, float]:
    """API legacy: calcula y registra los scores. Debe llamarse desde un contexto con span activo."""
    scores = compute_scores(query, answer)
    register_scores(scores)
    get_client().flush()
    return scores
