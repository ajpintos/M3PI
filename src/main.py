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

from langfuse import get_client, observe

from src.graph import app
from src.agents.evaluator import compute_scores, register_scores
from src.observability import build_callback, new_session_id


@observe(name="multi-agent-routing")
def _invoke_graph(query: str, session_id: str, callback, evaluate: bool = True) -> dict:
    """Ejecuta el grafo dentro de un trace de Langfuse.

    El scoring se hace ADENTRO del contexto del @observe porque en esta versión
    de langfuse v3, score_current_span() requiere un span activo en el contexto.
    """
    langfuse = get_client()

    result: dict = app.invoke(
        {"query": query, "intent": "", "answer": "", "domain_used": ""},
        config={"callbacks": [callback]},
    )

    # Enriquecer el span con metadata para depurar en Langfuse
    try:
        langfuse.update_current_span(
            input={"query": query},
            output={"answer": result.get("answer"), "intent": result.get("intent")},
            metadata={
                "session_id": session_id,
                "intent": result.get("intent"),
                "domain_used": result.get("domain_used"),
                "tags": ["routing", result.get("intent", "unknown").lower()],
            },
        )
    except Exception as exc:
        print(f"  [trace] No se pudo enriquecer el span: {exc}", file=sys.stderr)

    # Evaluador (BONUS): calcula scores y los registra en el span activo
    if evaluate:
        try:
            scores = compute_scores(query=result["query"], answer=result["answer"])
            register_scores(scores)
            result["_scores"] = scores
        except Exception as exc:
            print(f"  [evaluator] Error al evaluar: {exc}", file=sys.stderr)

    return result


def run_query(query: str, session_id: str, evaluate: bool = True) -> dict:
    callback = build_callback()
    langfuse = get_client()

    result = _invoke_graph(query, session_id, callback, evaluate=evaluate)

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
