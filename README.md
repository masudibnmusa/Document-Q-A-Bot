# 📄 Document Q&A Bot

A Retrieval-Augmented Generation (RAG) chatbot that lets you upload PDFs/documents, ask questions about them, and get answers with source citations.

## ✨ Features

- 📤 Upload PDFs/DOCX documents
- 🔍 Semantic search over document content
- 💬 Ask natural language questions
- 📌 Answers include citations (source doc + page number)
- ⚡ Fast local vector search (Chroma)

## 🏗️ Tech Stack

| Stage | Tool |
|---|---|
| Parsing | PyPDF2 / pdfplumber |
| Chunking | LangChain RecursiveCharacterTextSplitter |
| Embeddings | OpenAI `text-embedding-3` / sentence-transformers |
| Vector Store | ChromaDB |
| LLM | Claude API (Anthropic) |
| UI | Streamlit |

## 📁 Project Structure

document-qa-bot/
├── app/
│ ├── main.py # Entry point
│ ├── config.py # API keys, settings
│ ├── ingestion/ # Loading & chunking
│ ├── embeddings/ # Embedding generation
│ ├── vectorstore/ # Vector DB + retrieval
│ ├── generation/ # LLM calls + prompts
│ ├── qa_pipeline.py # Orchestration
│ └── utils/ # Citation formatting, logging
├── data/
│ ├── raw_docs/
│ ├── processed/
│ └── vector_db/
├── tests/
├── notebooks/
├── .env.example
├── requirements.txt
└── run.sh


## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/document-qa-bot.git
cd document-qa-bot
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
cp .env.example .env
```

Add your API keys to `.env`:

ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here


### 5. Run the app

```bash
streamlit run app/main.py
```

## 🧠 How It Works

1. **Upload** a PDF/document
2. **Loader** extracts raw text
3. **Chunker** splits text into overlapping chunks with metadata (page #, source)
4. **Embedder** converts chunks into vectors
5. **Vector Store** saves vectors for similarity search
6. User asks a question → query is embedded
7. **Retriever** finds top-k relevant chunks
8. **LLM** generates an answer using retrieved chunks as context
9. **Citation formatter** attaches source references to the final answer

## 🧪 Running Tests

```bash
pytest tests/
```

## 🗺️ Roadmap

- [ ] Add hybrid search (BM25 + semantic)
- [ ] Add reranking (Cohere Rerank / cross-encoder)
- [ ] Support multi-document comparison queries
- [ ] Deploy to Vercel/Render with Docker

## 📄 License

MIT
