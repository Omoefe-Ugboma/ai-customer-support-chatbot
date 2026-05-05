from app.services.embedding_service import get_embedding
from app.services.vector_store import vector_store
from app.services.rerank_service import rerank_results
from app.services.context_service import clean_context


def retrieve_context(query: str):
    query_embedding = get_embedding(query)

    # Step 1: Get raw results
    raw_results = vector_store.search_with_scores(query_embedding, k=5)

    # Step 2: Re-rank
    ranked = rerank_results(raw_results, top_k=3)

    # Step 3: Extract text
    chunks = [r["text"] for r in ranked]

    # Step 4: Clean
    context = clean_context(chunks)

    return context