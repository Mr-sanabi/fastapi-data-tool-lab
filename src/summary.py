def build_summary(records, title="Generated Data Summary", limit=2):
    if limit < 1:
        raise ValueError("limit must be at least 1")
    if not records:
        return {
        "title": title,
        "total_records": 0,
        "fields": [],
        "preview": []
    }

    return{
        "title": title,
        "total_records": len(records),
        "fields": sorted({field for record in records for field in record}),
        "preview": records[:limit]
    }
