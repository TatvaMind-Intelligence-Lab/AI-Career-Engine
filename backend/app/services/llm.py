import os
import json
import re
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


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
# LLM GENERATION ONLY
# -----------------------------
def generate_analysis(context, jd_text):
    """
    Only handles LLM generation
    No scoring, no retrieval, no chunking
    """

    # Safety: limit context size (prevents model breaking)
    context = context[:3000]

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
- Do NOT generate score
- Do NOT add explanations
- Output strictly valid JSON
- If unsure, return empty lists
"""

    try:
        response = model.generate_content(prompt)
        raw_text = response.text

        parsed = extract_json(raw_text)

        if parsed:
            return {
                "missing_keywords": parsed.get("missing_keywords", []),
                "suggestions": parsed.get("suggestions", []),
                "rewritten_points": parsed.get("rewritten_points", [])
            }

        else:
            print("\n❌ LLM RAW OUTPUT:\n", raw_text)

            return {
                "missing_keywords": [],
                "suggestions": ["LLM output parsing failed"],
                "rewritten_points": []
            }

    except Exception as e:
        print("\n❌ LLM ERROR:", str(e))

        return {
            "missing_keywords": [],
            "suggestions": ["LLM failed to respond"],
            "rewritten_points": []
        }