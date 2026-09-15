from typing import List
from sentence_transformers import SentenceTransformer

_model = None


def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def embed_texts(texts: List[str]) -> List[List[float]]:
    """Generate embeddings for a list of text chunks."""
    model = get_model()
    return model.encode(texts, show_progress_bar=False).tolist()


def embed_query(query: str) -> List[float]:
    """Generate embedding for a single query string."""
    model = get_model()
    return model.encode([query])[0].tolist()