from ..utils.chunking import chunk_resume
from .vector_store import store_resume_chunks
from .retrieval import retrieve_relevant_chunks

from .scorer import (
    keyword_match_score,
    semantic_similarity_score,
    section_score,
    final_score
)

from .llm import generate_analysis  # we'll create this


def run_rag_pipeline(resume_text, jd_text):
    """
    Main orchestration pipeline
    """

    # -------------------------
    # STEP 1: CHUNKING
    # -------------------------
    chunks = chunk_resume(resume_text)

    # -------------------------
    # STEP 2: VECTOR STORAGE
    # -------------------------
    store_resume_chunks(chunks)

    # -------------------------
    # STEP 3: RETRIEVAL
    # -------------------------
    relevant_chunks = retrieve_relevant_chunks(chunks, jd_text)

    context = "\n\n".join([chunk["text"] for chunk in relevant_chunks])

    # -------------------------
    # STEP 4: SCORING
    # -------------------------
    keyword_score = keyword_match_score(resume_text, jd_text)
    semantic_score = semantic_similarity_score(resume_text, jd_text)
    section_scores = section_score(chunks, jd_text)

    score = final_score(keyword_score, semantic_score, section_scores)

    # -------------------------
    # STEP 5: LLM GENERATION
    # -------------------------
    llm_output = generate_analysis(context, jd_text)

    # -------------------------
    # FINAL OUTPUT
    # -------------------------
    return {
        "analysis": {
            "score": score,
            "missing_keywords": llm_output.get("missing_keywords", []),
            "suggestions": llm_output.get("suggestions", []),
            "rewritten_points": llm_output.get("rewritten_points", [])
        },
        "retrieval": relevant_chunks,
        "debug": {
        "keyword_score": float(round(keyword_score, 3)),
        "semantic_score": float(round(semantic_score, 3)),
        "section_scores": {
            k: float(v) for k, v in section_scores.items()
        }
    }
    }