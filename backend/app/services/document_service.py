from app.services.embedding_service import get_embedding
from app.services.vector_store import vector_store


def add_documents(texts: list[str]):
    embeddings = []

    for text in texts:
        emb = get_embedding(text)
        embeddings.append(emb)

    vector_store.add(embeddings, texts)