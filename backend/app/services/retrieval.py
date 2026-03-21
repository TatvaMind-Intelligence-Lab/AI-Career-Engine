import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from .embedding import get_embedding


def retrieve_relevant_chunks(resume_chunks, jd_text, top_k=3, min_score=0.3):
    """
    Retrieve most relevant resume chunks using semantic similarity
    """

    # Step 1: Embed JD once
    jd_embedding = get_embedding(jd_text)
    
    # # debugging asnd logging are crucial for retrieval quality
    # print("\n🔍 JD Embedding Sample (first 10 values):")
    # print(jd_embedding[:10])

    # Step 2: Embed all chunks (batch is faster if supported)
    chunk_embeddings = [get_embedding(chunk) for chunk in resume_chunks]

    # Step 3: Compute similarities (vectorized)
    similarities = cosine_similarity(
        [jd_embedding],
        chunk_embeddings
    )[0]

    # Step 4: Pair chunks with scores
    scored_chunks = list(zip(resume_chunks, similarities))

    # Step 5: Filter low-quality chunks
    filtered_chunks = [
        (chunk, score)
        for chunk, score in scored_chunks
        if score >= min_score
    ]

    # Step 6: Sort by similarity (descending)
    filtered_chunks.sort(key=lambda x: x[1], reverse=True)

    # Step 7: Fallback if everything filtered out
    if not filtered_chunks:
        filtered_chunks = scored_chunks
        filtered_chunks.sort(key=lambda x: x[1], reverse=True)

    # Step 8: Select top_k
    top_chunks = filtered_chunks[:top_k]

    # 🔍 Debug logs (VERY useful)
    print("\n🔍 Top Retrieved Chunks:")
    for i, (chunk, score) in enumerate(top_chunks):
        print(f"{i+1}. Score: {score:.4f}")
        print(chunk[:120])
        print("-" * 40)

    return [chunk for chunk, _ in top_chunks]