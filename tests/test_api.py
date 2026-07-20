from fastapi.testclient import TestClient

from src.main import app
from src.summary import build_summary

client = TestClient(app)


def test_build_summary_uses_union_of_fields():
    result = build_summary([{"a": 1}, {"b": 2}], limit=1)
    assert result["fields"] == ["a", "b"]
    assert len(result["preview"]) == 1


def test_report_summary_endpoint():
    response = client.post("/report-summary?limit=1", json={"title": "Inventory", "records": [{"id": 1}, {"id": 2}]})
    assert response.status_code == 200
    assert response.json()["title"] == "Inventory"
    assert len(response.json()["preview"]) == 1


def test_limit_validation():
    response = client.post("/report-summary?limit=0", json={"records": []})
    assert response.status_code == 422
