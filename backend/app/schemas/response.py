from pydantic import BaseModel
from typing import List, Dict


class Analysis(BaseModel):
    score: int
    missing_keywords: List[str]
    suggestions: List[str]
    rewritten_points: List[str]


class APIResponse(BaseModel):
    status: str
    data: Analysis
    retrieval: list
    debug: Dict