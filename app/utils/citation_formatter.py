from typing import List, Dict


def format_citations(chunks: List[Dict]) -> List[str]:
    """Turn chunk metadata into readable citation strings."""
    seen = set()
    citations = []
    for c in chunks:
        meta = c["metadata"]
        source = meta.get("source", "unknown")
        page = meta.get("page_number", "N/A")
        key = (source, page)
        if key not in seen:
            seen.add(key)
            citations.append(f"{source} — page {page}")
    return citations