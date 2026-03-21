from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    job_description: str