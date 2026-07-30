import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("The environment variable DATABASE_URL is not set")

# Ensure the connection URL uses postgresql:// instead of postgres://
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

COLLECTION_NAME = "films_recommendations"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L12-v2"
