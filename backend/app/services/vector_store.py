import faiss
import numpy as np
from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


class VectorStore:
    def __init__(self):
        self.documents = []
        self.embeddings = None
        self.index = None
        self.dimension = 1536  # OpenAI embedding size

        print("[OK] VectorStore initialized")

    # =========================
    # 🔢 CREATE EMBEDDING
    # =========================
    def embed(self, texts: list[str]):
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=texts
        )
        return [e.embedding for e in response.data]

    # =========================
    # 📥 ADD DOCUMENTS
    # =========================
    def add_documents(self, texts: list[str]):
        if not texts:
            return

        new_embeddings = self.embed(texts)

        if self.embeddings is None:
            self.embeddings = np.array(new_embeddings).astype("float32")
        else:
            self.embeddings = np.vstack([
                self.embeddings,
                np.array(new_embeddings).astype("float32")
            ])

        self.documents.extend(texts)

        # Create / update FAISS index
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(self.embeddings)

        print(f"[OK] Added {len(texts)} documents to vector store")

    # =========================
    # 🔎 SEARCH
    # =========================
    def search(self, query: str, k: int = 5):
        if self.index is None or not self.documents:
            return []

        query_embedding = self.embed([query])[0]
        query_vector = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query_vector, k)

        results = []
        for idx in indices[0]:
            if 0 <= idx < len(self.documents):
                results.append(self.documents[idx])

        print(f"[OK] Retrieved {len(results)} results from vector store")

        return results

    # =========================
    # 🔄 RESET STORE
    # =========================
    def reset(self):
        self.documents = []
        self.embeddings = None
        self.index = None

        print("[OK] Vector store reset")


# Singleton instance
vector_store = VectorStore()