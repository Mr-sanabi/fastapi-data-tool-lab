def build_summary(records, title="Generated Data Summary", limit=2):
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
        "fields": list(records[0].keys()),
        "preview": records[:limit]
    }