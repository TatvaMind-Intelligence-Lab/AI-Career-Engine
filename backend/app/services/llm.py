import os
import json
import re
import google.generativeai as genai
from dotenv import load_dotenv

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
    prompt = f"""
You are an ATS optimization expert.

Analyze the resume against the job description.

Resume:
{resume_text}

Job Description:
{jd_text}

Return ONLY valid JSON.

STRICT RULES:
- No explanation
- No markdown
- No text outside JSON
- Ensure valid JSON format

Format:
{{
  "score": number,
  "missing_keywords": ["keyword1", "keyword2"],
  "suggestions": ["suggestion1", "suggestion2"],
  "rewritten_points": ["point1", "point2"]
}}

If unable to generate, return:
{{}}
"""

    try:
        response = model.generate_content(prompt)
        raw_text = response.text

        parsed = extract_json(raw_text)

        if parsed:
            return parsed
        else:
            return {
                "error": "Invalid JSON from model",
                "raw_output": raw_text
            }

    except Exception as e:
        return {
            "error": str(e)
        }