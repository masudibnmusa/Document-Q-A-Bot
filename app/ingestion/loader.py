from pathlib import Path
from typing import List, Dict
import pypdf


def load_pdf(file_path: str) -> str:
    """Extract raw text from a PDF file."""
    reader = pypdf.PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def load_pdf_with_pages(file_path: str) -> List[Dict]:
    """Extract text per page, useful for page-level citations."""
    reader = pypdf.PdfReader(file_path)
    pages = []
    for i, page in enumerate(reader.pages):
        pages.append({
            "page_number": i + 1,
            "text": page.extract_text() or ""
        })
    return pages


def load_docx(file_path: str) -> str:
    """Extract raw text from a DOCX file."""
    import docx
    doc = docx.Document(file_path)
    return "\n".join(p.text for p in doc.paragraphs)


def load_document(file_path: str) -> str:
    """Dispatch loader based on file extension."""
    ext = Path(file_path).suffix.lower()
    if ext == ".pdf":
        return load_pdf(file_path)
    elif ext == ".docx":
        return load_docx(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")