# FastAPI Data Tool Lab

A deliberately small learning lab that exposes reusable dataset-summary logic through a typed HTTP API.

> This repository is a lab, not a production service.

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/info` | Project metadata |
| `POST` | `/report-summary?limit=2` | Summarize JSON records and return a preview |

## Run locally

```bash
python -m pip install -r requirements.txt
uvicorn src.main:app --reload
```

Example request:

```json
{
  "title": "Customer export",
  "records": [{"id": 1, "name": "Ada"}, {"id": 2, "email": "grace@example.com"}]
}
```

The response reports the title, total records, a sorted union of fields, and a limited preview.

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Stack

Python, FastAPI, Pydantic, Uvicorn, pytest, HTTPX.
