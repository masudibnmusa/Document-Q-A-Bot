import os
from dotenv import load_dotenv

load_dotenv()

APP_TITLE = "Document Q&A Bot"

# API Keys
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Models
EMBEDDING_MODEL = "text-embedding-3-small"
LLM_MODEL = "claude-sonnet-4-6"

# Chunking
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Retrieval
TOP_K = 5

# Vector store
VECTOR_DB_DIR = "data/vector_db"