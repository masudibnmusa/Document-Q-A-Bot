import uuid
from app.ingestion.loader import load_pdf_with_pages
from app.ingestion.chunker import chunk_text
from app.ingestion.metadata import build_chunk_metadata
from app.embeddings.embedder import embed_texts
from app.vectorstore.store import VectorStore
from app.vectorstore.retriever import Retriever
from app.generation.prompt_templates import build_qa_prompt
from app.generation.llm import generate_answer
from app.utils.citation_formatter import format_citations


class QAPipeline:
    def __init__(self):
        self.store = VectorStore()
        self.retriever = Retriever(self.store)

    def ingest(self, uploaded_file):
        """Load, chunk, embed, and store an uploaded document."""
        doc_id = str(uuid.uuid4())
        source = uploaded_file.name

        # Save temp file
        temp_path = f"data/raw_docs/{source}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        pages = load_pdf_with_pages(temp_path)
        all_chunks, all_metadata = [], []

        for page in pages:
            chunks = chunk_text(page["text"])
            metas = build_chunk_metadata(chunks, source=source, doc_id=doc_id)
            for m in metas:
                m["page_number"] = page["page_number"]
            all_chunks.extend(chunks)
            all_metadata.extend(metas)

        embeddings = embed_texts(all_chunks)
        ids = [f"{doc_id}_{i}" for i in range(len(all_chunks))]

        self.store.add(ids=ids, embeddings=embeddings, metadatas=all_metadata, documents=all_chunks)

    def answer(self, query: str):
        """Retrieve relevant chunks and generate a cited answer."""
        chunks = self.retriever.retrieve(query)
        prompt = build_qa_prompt(query, chunks)
        answer_text = generate_answer(prompt)
        citations = format_citations(chunks)
        return answer_text, citations