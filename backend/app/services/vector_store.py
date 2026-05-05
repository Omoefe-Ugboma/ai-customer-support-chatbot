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

    def search(self, query_embedding, k=3):
        if len(self.texts) == 0:
            return []

        query = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query, k)

        results = []
        for i in indices[0]:
            if i < len(self.texts):
                results.append(self.texts[i])

        return results


# Singleton instance
vector_store = VectorStore()