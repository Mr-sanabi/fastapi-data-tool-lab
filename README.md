# FastAPI Data Tool Lab

A small learning API that summarizes JSON records. Not a production service.

## Run

```bash
python -m pip install -r requirements.txt
uvicorn src.main:app --reload
```

Send `POST /report-summary?limit=2` with:

```json
{"title": "Customer export", "records": [{"id": 1, "name": "Ada"}]}
```

The response contains the title, record count, combined field names, and a preview. `limit` accepts 1–100; `GET /info` returns project information.

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```
