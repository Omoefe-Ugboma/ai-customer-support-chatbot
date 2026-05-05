def clean_context(chunks: list[str]):
    seen = set()
    clean_chunks = []

    for chunk in chunks:
        c = chunk.strip()

        if c and c not in seen:
            clean_chunks.append(c)
            seen.add(c)

    return "\n".join(clean_chunks)