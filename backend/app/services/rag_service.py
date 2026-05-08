from openai import OpenAI
from app.core.config import settings
from app.services.vector_store import vector_store

client = OpenAI(api_key=settings.OPENAI_API_KEY)


# =========================
# 🧠 1. QUERY REWRITING
# =========================
def rewrite_query(query: str) -> str:
    """
    Convert vague user queries into clear semantic search queries
    Example:
    "How much do I pay?" → "What is the tuition fee?"
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Rewrite the user question into a clear, specific search query. "
                        "Keep it short and meaningful."
                    )
                },
                {"role": "user", "content": query}
            ],
            temperature=0
        )

        return response.choices[0].message.content.strip()

    except Exception:
        return query  # fallback


# =========================
# 🔎 2. KEYWORD FALLBACK
# =========================
def keyword_fallback(query: str, documents: list[str]) -> list[str]:
    """
    Simple keyword search if semantic search fails
    """
    results = []

    for doc in documents:
        if any(word.lower() in doc.lower() for word in query.split()):
            results.append(doc)

    return results[:5]


# =========================
# 🧠 3. CONTEXT RETRIEVAL
# =========================
def retrieve_context(query: str) -> str:
    """
    Full smart retrieval pipeline:
    1. Rewrite query
    2. Semantic search
    3. Keyword fallback
    """

    # 🔥 Step 1: Improve query
    improved_query = rewrite_query(query)

    print(f"[OK] Original Query: {query}")
    print(f"[OK] Rewritten Query: {improved_query}")

    # 🔥 Step 2: Semantic search
    results = vector_store.search(improved_query, k=5)

    # 🔥 Step 3: Fallback if no results
    if not results:
        print("[OK] Using keyword fallback...")
        results = keyword_fallback(query, vector_store.documents)

    # 🔥 Step 4: Return formatted context
    context = "\n".join(results) if results else ""

    print(f"[OK] Retrieved Context:\n{context}")

    return context