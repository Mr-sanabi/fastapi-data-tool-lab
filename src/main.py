from fastapi import FastAPI


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


