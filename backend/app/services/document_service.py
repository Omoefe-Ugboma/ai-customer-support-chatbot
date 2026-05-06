from app.services.embedding_service import get_embedding
from app.services.vector_store import vector_store
from app.services.chunking_service import split_text


def add_documents(texts: list[str]):
    all_chunks = []

    for text in texts:
        chunks = split_text(text)
        all_chunks.extend(chunks)

    embeddings = []

    for chunk in all_chunks:
        emb = get_embedding(chunk)
        embeddings.append(emb)

    vector_store.add_documents(all_chunks) 