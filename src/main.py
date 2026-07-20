from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Any
from src.summary import build_summary


app = FastAPI(
    title="FastAPI Data Tool Lab",
    description="First FastAPI lab for turning Python data tools into API endpoints.",
    version="0.1.0"
)


class SummaryRequest(BaseModel):
    records: list[dict[str, Any]] = Field(default_factory=list)
    title: str = "Generated Data Summary"


class SummaryResponse(BaseModel):
    title: str
    total_records: int
    fields: list[str]
    preview: list[dict[str, Any]]

@app.get("/info")
def get_info():
    return {
        "project": "FastAPI Data Tool Lab",
        "type": "tech unlock lab",
        "stack": ["Python", "FastAPI", "Uvicorn"],
        "goal": "Learn how to expose data-tool logic through API endpoints"
    }

@app.post("/report-summary", response_model=SummaryResponse)
def get_summary(payload: SummaryRequest, limit: int = Query(default=2, ge=1, le=100)):
    return build_summary(payload.records, payload.title, limit)
