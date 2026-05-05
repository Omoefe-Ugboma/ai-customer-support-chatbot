from app.services.embedding_service import get_embedding
from app.services.vector_store import vector_store


def retrieve_context(query: str):
    query_embedding = get_embedding(query)

    results = vector_store.search(query_embedding, k=3)

    return "\n".join(results)