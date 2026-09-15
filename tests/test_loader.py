import pytest
from app.ingestion.loader import load_pdf, load_pdf_with_pages, load_document


def test_load_pdf_returns_string(sample_pdf_path):
    text = load_pdf(sample_pdf_path)
    assert isinstance(text, str)
    assert len(text) > 0


def test_load_pdf_with_pages_structure(sample_pdf_path):
    pages = load_pdf_with_pages(sample_pdf_path)
    assert isinstance(pages, list)
    assert "page_number" in pages[0]
    assert "text" in pages[0]


def test_load_document_unsupported_extension():
    with pytest.raises(ValueError):
        load_document("file.xyz")


@pytest.fixture
def sample_pdf_path():
    # TODO: point to a small sample PDF in tests/fixtures/
    return "tests/fixtures/sample.pdf"