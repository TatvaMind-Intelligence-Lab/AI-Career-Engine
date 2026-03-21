import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# for m in genai.list_models():
#     print(m.name)

# Configure API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ Correct model
model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(resume_text, jd_text):
    prompt = f"""
You are an ATS optimization expert.

Compare the following resume with the job description.

Resume:
{resume_text}

Job Description:
{jd_text}

Return STRICTLY in this format:

Match Score: <number>
Missing Keywords: <comma separated list>
Suggestions:
- ...
- ...
Rewritten Bullet Points:
- ...
- ...
"""

    response = model.generate_content(prompt)

    return response.text
