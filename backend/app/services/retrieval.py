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

    # Pair chunks with scores
    scored_chunks = list(zip(resume_chunks, similarities))

    # Sort by similarity (high → low)
    scored_chunks.sort(key=lambda x: x[1], reverse=True)

    # Select top_k
    top_chunks = scored_chunks[:top_k]

    # Optional debug
    print("\n🔍 Top Retrieved Chunks:")
    for chunk, score in top_chunks:
        print(f"Score: {score:.4f}")
        print(chunk[:100], "\n")

    return [chunk for chunk, _ in top_chunks]