import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from .embedding import get_embedding


def retrieve_relevant_chunks(resume_chunks, jd_text, top_k=3):
    jd_embedding = get_embedding(jd_text)

    chunk_embeddings = [get_embedding(chunk) for chunk in resume_chunks]

    similarities = [
        cosine_similarity([jd_embedding], [chunk_emb])[0][0]
        for chunk_emb in chunk_embeddings
    ]

    # Get top-k chunks
    top_indices = np.argsort(similarities)[-top_k:][::-1]

    return [resume_chunks[i] for i in top_indices]