import os
import json
import re
import google.generativeai as genai
from dotenv import load_dotenv
from ..utils.chunking import chunk_resume
from .retrieval import retrieve_relevant_chunks
from .vector_store import store_resume_chunks

load_dotenv()

# Configure API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Model
model = genai.GenerativeModel("gemini-2.5-flash")  # safer than 2.5 for now


def extract_json(text):
    """
    Extract JSON from model response safely
    """
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
        return None
    except Exception:
        return None


def analyze_resume(resume_text, jd_text):
    # Step 1: Chunk
    chunks = chunk_resume(resume_text)

    # Step 2: Store in vector DB
    store_resume_chunks(chunks)

    # Step 3: Retrieve relevant chunks
    relevant_chunks = retrieve_relevant_chunks(chunks, jd_text)

    context = "\n\n".join([chunk["text"] for chunk in relevant_chunks])
    prompt = f"""
You are an expert ATS (Applicant Tracking System) analyzer.

Your job is to evaluate how well a candidate's resume matches a job description.

IMPORTANT:
- You are given ONLY the most relevant sections of the resume (not full resume)
- Base your analysis ONLY on this context
- Be precise and realistic

========================
Relevant Resume Sections:
{context}
========================

Job Description:
{jd_text}

========================

Return ONLY valid JSON:

{{
  "score": number (0-100),
  "missing_keywords": ["..."],
  "suggestions": ["..."],
  "rewritten_points": ["..."]
}}

Rules:
- Do NOT assume missing info outside context
- Do NOT add explanations outside JSON
- Keep suggestions actionable and concise
"""

    try:
        response = model.generate_content(prompt)
        raw_text = response.text

        parsed = extract_json(raw_text)

        if parsed:
            return {
                "analysis": parsed,
                "retrieval": relevant_chunks
            }
        else:
            return {
                "error": "Invalid JSON from model",
                "raw_output": raw_text
            }

    except Exception as e:
        return {
            "error": str(e)
        }