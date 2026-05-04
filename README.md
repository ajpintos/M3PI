# Sistema Multi-Agente de Routing con LangGraph + RAG + Langfuse

## Descripción del proyecto

Sistema de routing inteligente de tickets de soporte para una empresa SaaS. Un **Agente Orquestador** clasifica la intención de cada consulta (HR, TECH, FINANCE) y la enruta condicionalmente al **RAG Agent especializado** correspondiente, que responde basándose en la documentación interna de la empresa. Todo el flujo queda trazado en **Langfuse** para depuración y observability completa.

```
Usuario
  │
  ▼
[Orchestrator] ─── clasifica intención ───► HR / TECH / FINANCE / UNKNOWN
                                               │
                                               ▼
                                     [RAG Agent especializado]
                                      • Recupera chunks relevantes (Chroma)
                                      • Genera respuesta fundamentada (GPT-4o-mini)
                                               │
                                               ▼
                                      [Evaluator Agent] ── scores → Langfuse
```

### Arquitectura del StateGraph (LangGraph)

```
ENTRY ──► [classify] ──┬──► [hr]      ──► END
                       ├──► [tech]    ──► END
                       ├──► [finance] ──► END
                       └──► [fallback]──► END
```

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repo>
cd M3PI
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Configurar variables de entorno

```bash
cp .env.example .env
```

Edita `.env` con tus claves:

```env
OPENAI_API_KEY=sk-...               # OpenAI API key
LANGFUSE_PUBLIC_KEY=pk-lf-xxx       # Langfuse public key
LANGFUSE_SECRET_KEY=sk-lf-xxx       # Langfuse secret key
LANGFUSE_HOST=https://cloud.langfuse.com
```

Obtén las claves de Langfuse en [cloud.langfuse.com](https://cloud.langfuse.com) → Settings → API Keys.

---

## Setup de datos

### Paso 1: Generar documentos sintéticos

```bash
python scripts/generate_docs.py
```

Crea ~45 archivos `.md` en `data/hr_docs/`, `data/tech_docs/` y `data/finance_docs/`.

### Paso 2: Indexar en Chroma (requiere OPENAI_API_KEY)

```bash
python scripts/ingest.py
```

Chunkea los documentos (`chunk_size=500, overlap=50`), genera embeddings con `text-embedding-3-small` y persiste las colecciones en `data/chroma/`. Muestra el conteo de chunks por dominio (≥50 por colección).

---

## Ejecución

### Consulta individual

```bash
python -m src.main "¿Cuántos días de vacaciones tengo al año?"
python -m src.main "No puedo conectarme a la VPN"
python -m src.main "¿Cómo reporto un gasto de viaje?"
```

Salida de ejemplo:

```
────────────────────────────────────────────────────────────
  Intención detectada : HR
  Agente utilizado    : hr
────────────────────────────────────────────────────────────

Todo empleado de tiempo completo tiene derecho a 20 días hábiles de vacaciones anuales...
```

### Batch de pruebas

```bash
python -m src.main --batch test_queries.json
```

Ejecuta las 14 queries del archivo de pruebas y muestra una tabla de accuracy de routing:

```
────────────────────────────────────────────────────────────
QUERY                                         ESPERADO   OBTENIDO   OK
────────────────────────────────────────────────────────────
¿Cuántos días de vacaciones tengo al año?     HR         HR         ✓
No puedo conectarme a la VPN desde casa...    TECH       TECH       ✓
...
────────────────────────────────────────────────────────────
Accuracy de routing: 13/14 (92.9%)
```

### Sin evaluador (más rápido, sin llamadas extra a la API)

```bash
python -m src.main "tu consulta" --no-eval
```

---

## Observability en Langfuse

Cada invocación genera un trace en Langfuse con:
- **Span `classify`**: prompt del orchestrator + respuesta de intención
- **Span `retriever`**: documentos recuperados por Chroma
- **Span LLM**: prompt completo con contexto + respuesta final + tokens usados
- **Scores del evaluador**: relevance, completeness, accuracy, overall (1-10)

Para depurar misclassifications: filtra trazas por tag `unknown` en el dashboard de Langfuse.

---

## Decisiones técnicas

### ¿Por qué LangGraph en lugar de RouterChain?

`RouterChain` de LangChain clásico es un wrapper simple que oculta el estado y dificulta la depuración. LangGraph expone el estado explícito (`TypedDict`) en cada nodo, permite añadir nodos de validación o re-routing sin refactorizar, y genera un grafo visual inspeccionable. Además, el profesor enseñó este patrón directamente en `soporte_interno.py`.

### ¿Por qué Chroma como vector store?

Chroma funciona completamente en local sin infraestructura adicional (sin Docker, sin servidor), persiste en disco y se reconstruye con un solo comando. Para un proyecto educativo/demo es la opción con menor fricción operacional. En producción se reemplazaría por Pinecone o Weaviate con índices gestionados.

### Estrategia de chunking: chunk_size=500, overlap=50

500 tokens es suficiente para contener una política completa o un procedimiento paso a paso sin perder coherencia. El overlap de 50 tokens garantiza que las oraciones cortadas en el límite de chunk aparezcan en ambos chunks vecinos, evitando que el retriever pierda contexto relevante.

### k=4 en el retriever

Con k=4 se recuperan cuatro chunks distintos, suficientes para cubrir paráfrasis y distintas secciones del documento relevante, sin diluir la calidad de la respuesta con chunks irrelevantes que confundirían al LLM.

### ¿Por qué LLM-as-judge en lugar de métricas lexicales (BLEU, ROUGE)?

BLEU/ROUGE miden solapamiento de tokens, no relevancia semántica. Una respuesta correcta y completa que use sinónimos o restructure la información recibiría score bajo. El LLM-as-judge evalúa el significado, no la forma, y es extensible a nuevas dimensiones sin rediseño. El sesgo de autoindulgencia (mismo modelo que responde y evalúa) es una limitación conocida, mitigable usando un modelo diferente para el juez si se requiere mayor rigor.

---

## Limitaciones conocidas

- **Routing single-label**: el sistema asigna una única intención. Consultas multi-departamento ("necesito acceso al sistema de nómina") pueden clasificarse incorrectamente.
- **Sin re-ranking**: los chunks se recuperan por similitud coseno simple. En producción se beneficiaría de un re-ranker (cross-encoder) para mejorar la precisión del contexto.
- **Evaluador con sesgo de autoindulgencia**: el mismo modelo (`gpt-4o-mini`) que genera la respuesta también la evalúa. Para producción se recomienda usar `gpt-4o` como juez independiente.
- **Documentos sintéticos**: los docs de la colección son ficticios. La calidad del RAG mejora significativamente con documentos reales de la empresa.

---

## Estructura del proyecto

```
M3PI/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── test_queries.json
├── data/
│   ├── hr_docs/          # ~15 docs de RRHH (.md)
│   ├── tech_docs/        # ~15 docs de IT (.md)
│   ├── finance_docs/     # ~15 docs de Finanzas (.md)
│   └── chroma/           # vector store (gitignored)
├── scripts/
│   ├── generate_docs.py  # genera docs sintéticos
│   └── ingest.py         # embeddings + indexación en Chroma
└── src/
    ├── config.py          # LLM, embeddings, Langfuse handler
    ├── observability.py   # helpers de tracing
    ├── vector_store.py    # factory de retrievers Chroma
    ├── graph.py           # StateGraph LangGraph
    ├── main.py            # CLI
    └── agents/
        ├── orchestrator.py  # clasificador de intención
        ├── rag_agent.py     # RAG chain parametrizado por dominio
        └── evaluator.py     # LLM-as-judge + Langfuse scores
```
