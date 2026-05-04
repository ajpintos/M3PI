"""
Chunkea los documentos de cada dominio y los persiste en Chroma.
Idempotente: si la colección ya tiene el mismo número de documentos, salta el dominio.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

load_dotenv()

BASE_DIR = Path(__file__).parent.parent / "data"
CHROMA_DIR = BASE_DIR / "chroma"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

DOMAINS = ["hr", "tech", "finance"]


def ingest_domain(domain: str, embeddings: OpenAIEmbeddings) -> None:
    docs_path = BASE_DIR / f"{domain}_docs"
    collection_name = f"{domain}_docs"

    loader = DirectoryLoader(
        str(docs_path),
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )
    raw_docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    chunks = splitter.split_documents(raw_docs)

    vectorstore = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=str(CHROMA_DIR),
    )

    existing = vectorstore.get()
    existing_count = len(existing["ids"])

    if existing_count == len(chunks):
        print(f"[{domain}] Ya indexado ({existing_count} chunks). Omitiendo.")
        return

    if existing_count > 0:
        vectorstore.delete_collection()
        vectorstore = Chroma(
            collection_name=collection_name,
            embedding_function=embeddings,
            persist_directory=str(CHROMA_DIR),
        )

    vectorstore.add_documents(chunks)
    print(f"[{domain}] Indexados {len(chunks)} chunks desde {len(raw_docs)} documentos.")


def main() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY no está configurado en .env")

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    CHROMA_DIR.mkdir(parents=True, exist_ok=True)

    for domain in DOMAINS:
        docs_path = BASE_DIR / f"{domain}_docs"
        if not docs_path.exists() or not any(docs_path.glob("*.md")):
            print(f"[{domain}] No se encontraron documentos en {docs_path}. Ejecuta generate_docs.py primero.")
            continue
        ingest_domain(domain, embeddings)

    print("\nIngestión completada.")


if __name__ == "__main__":
    main()
