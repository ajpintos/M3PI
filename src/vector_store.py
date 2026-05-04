from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.vectorstores import VectorStoreRetriever

from src.config import get_embeddings

CHROMA_DIR = Path(__file__).parent.parent / "data" / "chroma"
VALID_DOMAINS = {"hr", "tech", "finance"}


def get_retriever(domain: str, k: int = 4) -> VectorStoreRetriever:
    if domain not in VALID_DOMAINS:
        raise ValueError(f"Dominio inválido '{domain}'. Válidos: {VALID_DOMAINS}")

    vectorstore = Chroma(
        collection_name=f"{domain}_docs",
        embedding_function=get_embeddings(),
        persist_directory=str(CHROMA_DIR),
    )
    return vectorstore.as_retriever(search_kwargs={"k": k})
