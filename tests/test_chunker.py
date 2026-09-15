from app.ingestion.chunker import chunk_text


def test_chunk_text_returns_list():
    text = "This is a sentence. " * 100
    chunks = chunk_text(text, chunk_size=100, chunk_overlap=20)
    assert isinstance(chunks, list)
    assert len(chunks) > 1


def test_chunk_text_respects_overlap():
    text = "word " * 500
    chunks = chunk_text(text, chunk_size=200, chunk_overlap=50)
    assert all(len(c) <= 250 for c in chunks)  # rough upper bound check


def test_chunk_empty_text():
    chunks = chunk_text("")
    assert chunks == [] or chunks == [""]