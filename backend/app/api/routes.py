from unittest import result
from fastapi import APIRouter, UploadFile, File, Form
from ..services.parser import extract_text
from ..services.ragpipeline import run_rag_pipeline

router = APIRouter()

@router.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        resume_text = extract_text(resume)

        result = run_rag_pipeline(resume_text, job_description)

        return {
        "status": "success",
        "data": result["analysis"],   # ✅ flatten
        "retrieval": result.get("retrieval", []),
        "debug": result.get("debug", {})
    }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }