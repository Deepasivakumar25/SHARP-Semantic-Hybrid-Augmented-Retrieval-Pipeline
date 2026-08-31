def combine_hybrid_indices(semantic_indices: list[int], keyword_indices: list[int]) -> list[int]:
    combined = semantic_indices + keyword_indices
    return list(dict.fromkeys(combined))


def build_context(chunk_list: list[str], hybrid_indices: list[int]) -> str:
    hybrid_chunks = [chunk_list[idx] for idx in hybrid_indices]
    return "\n\n".join(hybrid_chunks)
