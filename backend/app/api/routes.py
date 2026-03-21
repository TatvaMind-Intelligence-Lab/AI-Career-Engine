from fastapi import APIRouter, UploadFile, File, Form
from app.services.parser import extract_text
from app.services.llm import analyze_resume

router = APIRouter()

@router.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        resume_text = extract_text(resume)

        result = analyze_resume(resume_text, job_description)

        return {
            "status": "success",
            "analysis": result
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }