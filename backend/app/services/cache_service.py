cache = {}


# =========================
# GET CACHE
# =========================
def get_cached(
    session_id: str,
    query: str
):

    return cache.get(
        f"{session_id}:{query}"
    )


# =========================
# SET CACHE
# =========================
def set_cache(
    session_id: str,
    query: str,
    response: str
):

    cache[
        f"{session_id}:{query}"
    ] = response


# =========================
# CLEAR CACHE
# =========================
def clear_cache():
    cache.clear()