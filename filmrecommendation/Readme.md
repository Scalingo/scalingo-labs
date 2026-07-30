# Film Recommendation Engine with pgvector and LangChain

A sample movie recommendation system that uses vector embeddings and similarity
search to suggest films based on a natural-language description. It is powered
by PostgreSQL® with the [pgvector](https://github.com/pgvector/pgvector)
extension and [LangChain](https://www.langchain.com/), served by a small
FastAPI application.

> This project is the companion code for the Scalingo tutorial
> **[Build a Recommendation System with pgvector](https://doc.scalingo.com/tutorials/pgvector-recommendation)**.
> Follow the tutorial for a guided, step-by-step deployment on Scalingo.

## How It Works

1. Each film description is converted into a vector embedding.
2. Embeddings are stored in a PostgreSQL® database using the pgvector extension.
3. When a user submits a query, it is embedded the same way.
4. The API performs a vector similarity search and returns the closest matches.

## Tech Stack

- **FastAPI** — web framework serving the API and the search interface
- **LangChain** + **langchain-postgres** — embeddings and `PGVector` vector store
- **HuggingFace** `sentence-transformers/all-MiniLM-L12-v2` — embedding model
- **PostgreSQL®** with **pgvector** — vector storage and similarity search
- **uv** — Python dependency management

## API Endpoints

| Method | Path              | Description                                  |
|--------|-------------------|----------------------------------------------|
| `GET`  | `/`               | Search interface (HTML)                      |
| `GET`  | `/health`         | Health check                                 |
| `POST` | `/recommendations`| Get similar films from a text description    |
| `GET`  | `/docs`           | Interactive API documentation (Swagger UI)   |

## Tutorial

Read the full step-by-step guide on Scalingo's documentation:

**[Build a Recommendation System with pgvector](https://doc.scalingo.com/tutorials/pgvector-recommendation)**