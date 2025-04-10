import difflib
from core.models import SourceCatalog

def find_sources_for_schema_fields(schema_fields):
    mappings = []

    all_source_fields = list(SourceCatalog.objects.values("source_field", "source_system", "description"))

    for target in schema_fields:
        best_match = difflib.get_close_matches(target["field"], [s["source_field"] for s in all_source_fields], n=1)
        if best_match:
            match_field = best_match[0]
            match_info = next(s for s in all_source_fields if s["source_field"] == match_field)
            mappings.append({
                "target": target["field"],
                "source": match_info["source_field"],
                "source_system": match_info["source_system"],
                "description": match_info["description"]
            })
        else:
            mappings.append({
                "target": target["field"],
                "source": "NOT FOUND",
                "source_system": "UNKNOWN",
                "description": "No match found"
            })

    return mappings
