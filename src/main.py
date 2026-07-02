from fastapi import FastAPI
from typing import List, Dict, Any


app = FastAPI(
    title="FastAPI Data Tool Lab",
    description="First FastAPI lab for turning Python data tools into API endpoints.",
    version="0.1.0"
)

@app.get("/info")
def get_info():
    return {
        "project": "FastAPI Data Tool Lab",
        "type": "tech unlock lab",
        "stack": ["Python", "FastAPI", "Uvicorn"],
        "goal": "Learn how to expose data-tool logic through API endpoints"
    }

@app.post("/report-summary")
def get_summary(records: List[Dict[str, Any]], limit: int = 2):
    if not records:
        return {
        "title": "Generated Data Summary",
        "total_records": 0,
        "fields": [],
        "preview": []
    }

    fields = list(records[0].keys())

    return{
        "title": "Generated Data Summary",
        "total_records": len(records),
        "fields": fields,
        "preview": records[:limit]
    }