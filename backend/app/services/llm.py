import os
import json
import re
import google.generativeai as genai
from dotenv import load_dotenv

from ..utils.chunking import chunk_resume
from .retrieval import retrieve_relevant_chunks
from .vector_store import store_resume_chunks

from ..services.scorer import (
    keyword_match_score,
    semantic_similarity_score,
    section_score,
    final_score
)

load_dotenv()

# Configure API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash-latest")


# -----------------------------
# JSON EXTRACTOR
# -----------------------------
def extract_json(text):
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
        return None
    except Exception:
        return None


# -----------------------------
# MAIN PIPELINE
# -----------------------------
def analyze_resume(resume_text, jd_text):

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
    # STEP 4: SCORING ENGINE
    # -------------------------
    keyword_score = keyword_match_score(resume_text, jd_text)
    semantic_score = semantic_similarity_score(resume_text, jd_text)
    section_scores = section_score(chunks, jd_text)

    score = final_score(keyword_score, semantic_score, section_scores)

    # -------------------------
    # STEP 5: LLM ANALYSIS
    # -------------------------
    prompt = f"""
You are an expert ATS (Applicant Tracking System) analyzer.

Evaluate the resume against the job description using ONLY the given context.

========================
Relevant Resume Sections:
{context}
========================

Job Description:
{jd_text}

========================

Return ONLY valid JSON:

{{
  "missing_keywords": ["..."],
  "suggestions": ["..."],
  "rewritten_points": ["..."]
}}

Rules:
- Do NOT generate score (score is computed separately)
- Do NOT add extra text
- Output strictly JSON
"""

    try:
        response = model.generate_content(prompt)
        raw_text = response.text

        parsed = extract_json(raw_text)

        if parsed:
            return {
                "analysis": {
                    "score": score,
                    "missing_keywords": parsed.get("missing_keywords", []),
                    "suggestions": parsed.get("suggestions", []),
                    "rewritten_points": parsed.get("rewritten_points", [])
                },
                "retrieval": relevant_chunks,
                "debug": {
                    "keyword_score": round(keyword_score, 3),
                    "semantic_score": round(semantic_score, 3),
                    "section_scores": section_scores
                }
            }

        else:
            print("\n❌ RAW MODEL OUTPUT:\n", raw_text)

            return {
                "analysis": {
                    "score": score,
                    "missing_keywords": [],
                    "suggestions": ["Model failed to generate structured output"],
                    "rewritten_points": []
                },
                "retrieval": relevant_chunks
            }

    except Exception as e:
        return {
            "error": str(e)
        }