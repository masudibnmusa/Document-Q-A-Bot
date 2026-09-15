from typing import List, Dict
from app.vectorstore.store import VectorStore
from app.embeddings.embedder import embed_query
from app.config import TOP_K


class Retriever:
    def __init__(self, store: VectorStore):
        self.store = store

    def retrieve(self, query: str, top_k: int = TOP_K) -> List[Dict]:
        """Embed query, run similarity search, return chunks with metadata."""
        query_embedding = embed_query(query)
        results = self.store.query(query_embedding, top_k=top_k)

        chunks = []
        docs = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        for doc, meta, dist in zip(docs, metadatas, distances):
            chunks.append({
                "text": doc,
                "metadata": meta,
                "score": dist
            })
        return chunks

    def rerank(self, query: str, chunks: List[Dict]) -> List[Dict]:
        """Optional: reorder chunks using a cross-encoder or Cohere Rerank."""
        # TODO: plug in reranking model if needed
        return chunks