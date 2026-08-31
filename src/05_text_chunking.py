def create_chunks(text: str, chunk_size: int = 50) -> list[str]:
    words = text.split()
    chunk_list = []
    for i in range(0, len(words), chunk_size):
        chunk_list.append(" ".join(words[i:i + chunk_size]))
    return chunk_list
