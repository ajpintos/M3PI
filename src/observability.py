import os
import uuid

from langfuse import Langfuse, get_client
from langfuse.langchain import CallbackHandler


def new_session_id() -> str:
    return str(uuid.uuid4())


def get_langfuse_client() -> Langfuse:
    """Devuelve el singleton del cliente Langfuse v3 (configurado vía env vars)."""
    return get_client()


def build_callback() -> CallbackHandler:
    """En Langfuse v3 el CallbackHandler no recibe argumentos.
    El enriquecimiento del trace (session_id, tags, metadata) se hace mediante
    span.update_trace() dentro del context manager en main.py."""
    return CallbackHandler()
