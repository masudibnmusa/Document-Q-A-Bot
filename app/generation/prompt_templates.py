from typing import List, Dict


CITATION_SYSTEM_PROMPT = """You are a helpful assistant answering questions based only on the provided document excerpts.

Rules:
- Only use information from the provided context.
- If the answer isn't in the context, say you don't know.
- After each claim, cite the source using [Source: {source}, Page: {page}].
- Be concise and accurate.
"""


def build_qa_prompt(query: str, chunks: List[Dict]) -> str:
    """Build the user prompt with retrieved context + citation instructions."""
    context_blocks = []
    for c in chunks:
        meta = c["metadata"]
        source = meta.get("source", "unknown")
        page = meta.get("page_number", "N/A")
        context_blocks.append(f"[Source: {source}, Page: {page}]\n{c['text']}")

    context = "\n\n---\n\n".join(context_blocks)

    return f"""Context:
{context}

Question: {query}

Answer the question using only the context above, citing sources as instructed."""