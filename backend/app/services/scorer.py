import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from .embedding import get_embedding


# -----------------------------
# 1. KEYWORD EXTRACTION
# -----------------------------
def extract_keywords(text):
    words = re.findall(r"\b[a-zA-Z]{2,}\b", text.lower())

    stopwords = {"and", "or", "the", "with", "a", "to", "of", "in"}
    keywords = [w for w in words if w not in stopwords]

    return set(keywords)


# -----------------------------
# 2. KEYWORD MATCH %
# -----------------------------
def keyword_match_score(resume_text, jd_text):
    jd_keywords = extract_keywords(jd_text)
    resume_keywords = extract_keywords(resume_text)

    if not jd_keywords:
        return 0.0

    match = jd_keywords.intersection(resume_keywords)

    return float(len(match) / len(jd_keywords))


# -----------------------------
# 3. SEMANTIC SIMILARITY
# -----------------------------
def semantic_similarity_score(resume_text, jd_text):
    embeddings = get_embedding([resume_text, jd_text])

    sim = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return float(sim)   # ✅ FIXED


# -----------------------------
# 4. SECTION-WISE SCORING
# -----------------------------
def section_score(chunks, jd_text):
    section_scores = {
        "skills": [],
        "experience": [],
        "projects": [],
        "other": []
    }

    jd_embedding = get_embedding([jd_text])[0]

    for chunk in chunks:
        emb = get_embedding([chunk])[0]
        score = cosine_similarity([jd_embedding], [emb])[0][0]

        chunk_upper = chunk.upper()

        if "[SKILLS]" in chunk_upper:
            section_scores["skills"].append(score)
        elif "[EXPERIENCE]" in chunk_upper:
            section_scores["experience"].append(score)
        elif "[PROJECTS]" in chunk_upper:
            section_scores["projects"].append(score)
        else:
            section_scores["other"].append(score)

    # ✅ FIXED
    return {
        key: float(np.mean(vals)) if vals else 0.0
        for key, vals in section_scores.items()
    }


# -----------------------------
# 5. FINAL WEIGHTED SCORE
# -----------------------------
def final_score(keyword_score, semantic_score, section_scores):

    weights = {
        "keyword": 0.3,
        "semantic": 0.3,
        "skills": 0.2,
        "experience": 0.1,
        "projects": 0.1
    }

    score = (
        keyword_score * weights["keyword"] +
        semantic_score * weights["semantic"] +
        section_scores.get("skills", 0) * weights["skills"] +
        section_scores.get("experience", 0) * weights["experience"] +
        section_scores.get("projects", 0) * weights["projects"]
    )

    return int(float(score) * 100)