import chromadb
from typing import List, Dict
from app.config import VECTOR_DB_DIR


class VectorStore:
    def __init__(self, collection_name: str = "documents"):
        self.client = chromadb.PersistentClient(path=VECTOR_DB_DIR)
        self.collection = self.client.get_or_create_collection(collection_name)

    def add(self, ids: List[str], embeddings: List[List[float]], metadatas: List[Dict], documents: List[str]):
        """Add chunks + embeddings + metadata to the store."""
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            metadatas=metadatas,
            documents=documents
        )

    def query(self, query_embedding: List[float], top_k: int = 5) -> Dict:
        """Run similarity search and return top-k matches."""
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

    def delete_collection(self):
        self.client.delete_collection(self.collection.name)