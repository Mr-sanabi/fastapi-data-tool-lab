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

@app.get("/report-summary")
def get_summary():
    records = [
        {
            "product_title": "Black Shirt",
            "price": "29.99",
            "sku": "SKU001"
        },
        {
            "product_title": "White Shirt",
            "price": "24.99",
            "sku": "SKU002"
        },
        {
            "product_title": "Blue Hoodie",
            "price": "49.99",
            "sku": "SKU003"
        }
    ]
    fields = list(records[0].keys())
    return{
        "title": "Sample Data Report",
        "total_records": len(records),
        "fields": fields,
        "preview": records[:2]
    }