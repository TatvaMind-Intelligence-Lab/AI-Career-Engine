import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from .embedding import get_embedding


def keyword_overlap_score(chunk, jd_text):
    """
    Simple keyword overlap boost
    """
    jd_words = set(jd_text.lower().split())
    chunk_words = set(chunk.lower().split())

    overlap = jd_words.intersection(chunk_words)

    return len(overlap) / (len(jd_words) + 1)


def section_weight(chunk):
    """
    Assign importance based on section
    """
    chunk_upper = chunk.upper()

    if "[SKILLS]" in chunk_upper:
        return 1.2
    elif "[EXPERIENCE]" in chunk_upper:
        return 1.1
    elif "[PROJECTS]" in chunk_upper:
        return 1.05
    elif "[EDUCATION]" in chunk_upper:
        return 0.9
    else:
        return 1.0


def retrieve_relevant_chunks(resume_chunks, jd_text, top_k=3, min_score=0.25):
    """
    Hybrid retrieval:
    - semantic similarity
    - keyword overlap
    - section weighting
    """

    # Step 1: Embed JD
    jd_embedding = get_embedding([jd_text])[0]

    # Step 2: Batch embed chunks (FASTER)
    chunk_embeddings = get_embedding(resume_chunks)

    # Step 3: Semantic similarity
    semantic_scores = cosine_similarity(
        [jd_embedding],
        chunk_embeddings
    )[0]

    scored_chunks = []

    for chunk, semantic_score in zip(resume_chunks, semantic_scores):

        # Step 4: Keyword score
        keyword_score = keyword_overlap_score(chunk, jd_text)

        # Step 5: Section weight
        weight = section_weight(chunk)

        # Step 6: Final hybrid score
        final_score = (0.7 * semantic_score + 0.3 * keyword_score) * weight

        scored_chunks.append((chunk, final_score, semantic_score, keyword_score))

    # Step 7: Filter low-quality
    filtered = [c for c in scored_chunks if c[1] >= min_score]

    if not filtered:
        filtered = scored_chunks

    # Step 8: Sort
    filtered.sort(key=lambda x: x[1], reverse=True)

    top_chunks = filtered[:top_k]

    # 🔍 Debug logs
    print("\n🧠 Hybrid Retrieval Results:")
    for i, (chunk, final, sem, key) in enumerate(top_chunks):
        print(f"{i+1}. Final: {final:.4f} | Semantic: {sem:.4f} | Keyword: {key:.4f}")
        print(chunk[:120])
        print("-" * 50)

    return [
        {
            "text": chunk,
            "final_score": float(final),
            "semantic_score": float(sem),
            "keyword_score": float(key)
        }
        for chunk, final, sem, key in top_chunks
    ]