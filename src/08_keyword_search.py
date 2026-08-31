import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def keyword_search(question: str, chunk_list: list[str], top_k: int = 3):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(chunk_list)
    question_tfidf = tfidf_vectorizer.transform([question])
    similarity_scores = cosine_similarity(question_tfidf, tfidf_matrix)
    top_indices = np.argsort(similarity_scores[0])[::-1][:top_k]
    keyword_chunk = [chunk_list[rec] for rec in top_indices]
    return keyword_chunk, top_indices.tolist()
