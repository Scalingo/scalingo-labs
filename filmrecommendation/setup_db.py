from src.database.vector_store import vector_store_manager


def setup_db():
    vector_store_manager.setup_database()

if __name__ == "__main__":
    setup_db()
