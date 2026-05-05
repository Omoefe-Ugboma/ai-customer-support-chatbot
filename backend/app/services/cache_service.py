cache = {}


def get_cached(query: str):
    return cache.get(query)


def set_cache(query: str, response: str):
    cache[query] = response