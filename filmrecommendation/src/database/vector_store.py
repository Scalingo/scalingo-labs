import psycopg2
from langchain_postgres import PGVector
from langchain_huggingface import HuggingFaceEmbeddings
from typing import List, Dict, Any

from ..config.settings import DATABASE_URL, COLLECTION_NAME, EMBEDDING_MODEL
from ..data.sample_films import FILMS_DATA


class VectorStoreManager:
    """Manager for the PostgreSQL vector database with pgvector"""
    
    def __init__(self):
        self.embeddings = None
        self.vector_store = None
        self._initialize_embeddings()
        self._initialize_vector_store()
    
    def _initialize_embeddings(self):
        """Initialize the HuggingFace embeddings model"""
        try:
            self.embeddings = HuggingFaceEmbeddings(
                model_name=EMBEDDING_MODEL,
                model_kwargs={'device': 'cpu'}
            )
            print("Embeddings model initialized successfully")
        except Exception as e:
            print(f"Error while initializing embeddings model: {e}")
            raise
    
    def _initialize_vector_store(self):
        """Initialize the PGVector vector store"""
        try:
            self.vector_store = PGVector(
                embeddings=self.embeddings,
                collection_name=COLLECTION_NAME,
                connection=DATABASE_URL
            )
            print("Vector store initialized successfully")
        except Exception as e:
            print(f"Error while initializing vector store: {e}")
            raise
    
    def setup_database(self):
        """Set up the database and insert sample data"""
        try:
            print("Connecting to the database...")
            conn = psycopg2.connect(DATABASE_URL)
            print("Database connection successful")
            
            cur = conn.cursor()
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
            conn.commit()
            cur.close()
            conn.close()
            print("vector extension installed")
            
            # Prepare data
            descriptions = [film["description"] for film in FILMS_DATA]
            metadatas = [{
                "title": film["title"],
                "image_url": film.get("image_url", "")
            } for film in FILMS_DATA]
            
            print(f"Adding data to the database... length: {len(descriptions)}")
            
            # Insert data into the vector store
            PGVector.from_texts(
                embedding=self.embeddings,
                texts=descriptions,
                metadatas=metadatas,
                collection_name=COLLECTION_NAME,
                connection=DATABASE_URL,
                pre_delete_collection=True
            )
            print("Data added successfully")
            
        except psycopg2.Error as e:
            print(f"Error while installing vector extension: {e}")
            raise
        except Exception as e:
            print(f"Error while inserting data: {e}")
            raise
    
    def similarity_search(self, query: str, k: int = 3) -> List[Dict[str, Any]]:
        """Perform a similarity search in the vector store"""
        if not self.vector_store:
            raise ValueError("The vector store is not initialized")
        
        try:
            similar_docs = self.vector_store.similarity_search(query, k=k)
            results = [{
                "title": doc.metadata.get("title", "Untitled"),
                "description": doc.page_content,
                "image_url": doc.metadata.get("image_url", "")
            } for doc in similar_docs]
            
            return results
        except Exception as e:
            print(f"Error during similarity search: {e}")
            raise


# Global instance of the vector store manager
vector_store_manager = VectorStoreManager()
