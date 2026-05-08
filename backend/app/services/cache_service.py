cache = {}


# =========================
# GET CACHE
# =========================
def get_cached(
    thread_id: str,
    query: str
):

    return cache.get(
        f"{thread_id}:{query}"
    )


# =========================
# SET CACHE
# =========================
def set_cache(
    thread_id: str,
    query: str,
    response: str
):

    cache[
        f"{thread_id}:{query}"
    ] = response


# =========================
# CLEAR CACHE
# =========================
def clear_cache():
    cache.clear()