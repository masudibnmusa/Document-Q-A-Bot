import pytest
from unittest.mock import MagicMock
from app.vectorstore.retriever import Retriever


def test_retrieve_returns_chunks_with_metadata():
    mock_store = MagicMock()
    mock_store.query.return_value = {
        "documents": [["chunk one", "chunk two"]],
        "metadatas": [[{"source": "doc.pdf", "page_number": 1}, {"source": "doc.pdf", "page_number": 2}]],
        "distances": [[0.1, 0.2]]
    }

    retriever = Retriever(mock_store)
    results = retriever.retrieve("test query", top_k=2)

    assert len(results) == 2
    assert results[0]["text"] == "chunk one"
    assert results[0]["metadata"]["page_number"] == 1


def test_rerank_returns_same_length_by_default():
    retriever = Retriever(store=MagicMock())
    chunks = [{"text": "a"}, {"text": "b"}]
    result = retriever.rerank("query", chunks)
    assert len(result) == len(chunks)