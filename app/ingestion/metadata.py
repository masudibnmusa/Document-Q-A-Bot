from typing import List, Dict


def build_chunk_metadata(chunks: List[str], source: str, doc_id: str) -> List[Dict]:
    """Attach source/doc_id/chunk_index metadata to each chunk."""
    return [
        {
            "text": chunk,
            "source": source,
            "doc_id": doc_id,
            "chunk_index": i
        }
        for i, chunk in enumerate(chunks)
    ]