from fastapi import APIRouter, UploadFile, File, Form, Depends
from fastapi import HTTPException
import asyncio

from app.services.parser import extract_text
from app.services.ragpipeline import run_rag_pipeline

from app.core.executor import executor
from app.core.logger import logger
from app.core.exception import TatvaMindError

from app.schemas.response import APIResponse

router = APIRouter()


@router.post("/analyze", response_model=APIResponse)
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        # -------------------------
        # INPUT VALIDATION
        # -------------------------
        if not resume:
            raise TatvaMindError("Resume file is required")

        if not job_description or len(job_description.strip()) < 10:
            raise TatvaMindError("Job description too short")

        logger.info("📥 Request received")

        # -------------------------
        # PARSE FILE
        # -------------------------
        resume_text = extract_text(resume)

        if not resume_text or len(resume_text.strip()) < 20:
            raise TatvaMindError("Invalid resume content")

        # -------------------------
        # ASYNC + EXECUTOR (NON-BLOCKING)
        # -------------------------
        loop = asyncio.get_running_loop()

        result = await asyncio.wait_for(
            loop.run_in_executor(
                executor,
                run_rag_pipeline,
                resume_text,
                job_description
            ),
            timeout=30  # ⏱️ timeout protection
        )

        logger.info("✅ Pipeline completed")

        # -------------------------
        # RESPONSE
        # -------------------------
        return APIResponse(
            status="success",
            data=result.get("analysis", {}),
            retrieval=result.get("retrieval", []),
            debug=result.get("debug", {})
        )

    except asyncio.TimeoutError:
        logger.error("⏱️ Request timeout")

        raise HTTPException(
            status_code=504,
            detail="Processing timeout (took too long)"
        )

    except TatvaMindError as e:
        logger.warning(f"⚠️ User error: {e.message}")

        raise HTTPException(
            status_code=400,
            detail=e.message
        )

    except Exception as e:
        logger.error(f"❌ Unexpected error: {str(e)}")

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )