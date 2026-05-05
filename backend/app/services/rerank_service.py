def rerank_results(results: list, top_k: int = 3):
    """
    Lower score = better match (FAISS L2)
    """
    sorted_results = sorted(results, key=lambda x: x["score"])
    return sorted_results[:top_k]