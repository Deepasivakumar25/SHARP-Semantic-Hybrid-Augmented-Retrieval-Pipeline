import numpy as np


def semantic_search(question: str, embedding_model, index, chunk_list: list[str], top_k: int = 3):
    question_embedding = embedding_model.encode([question])
    distance, index_number = index.search(np.array(question_embedding), k=top_k)
    retrieved_chunks = [chunk_list[idx] for idx in index_number[0]]
    return retrieved_chunks, index_number[0].tolist()
