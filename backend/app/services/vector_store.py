import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim: int = 1536):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, embeddings, texts):
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)
        self.texts.extend(texts)

    # ✅ NEW METHOD (THIS IS WHAT YOU WERE MISSING)
    def search_with_scores(self, query_embedding, k=5):
        if len(self.texts) == 0:
            return []

        query = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query, k)

        results = []

        for i, idx in enumerate(indices[0]):
            if idx < len(self.texts):
                results.append({
                    "text": self.texts[idx],
                    "score": float(distances[0][i])
                })

        return results


# Singleton instance
vector_store = VectorStore()


# Singleton instance
vector_store = VectorStore()

def search_with_scores(self, query_embedding, k=5):
    if len(self.texts) == 0:
        return []

    query = np.array([query_embedding]).astype("float32")
    distances, indices = self.index.search(query, k)

    results = []

    for i, idx in enumerate(indices[0]):
        if idx < len(self.texts):
            results.append({
                "text": self.texts[idx],
                "score": float(distances[0][i])
            })

    return results