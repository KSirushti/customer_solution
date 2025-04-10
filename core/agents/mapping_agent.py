def generate_mapping_table(source_discoveries):
    mappings = []

    for item in source_discoveries:
        if item["source"] == "NOT FOUND":
            transformation = "manual_check_required"
        elif item["source"] == item["target"]:
            transformation = "direct_map"
        else:
            transformation = "simple_transformation"

        mappings.append({
            "source": item["source"],
            "target": item["target"],
            "source_system": item["source_system"],
            "transformation": transformation
        })

    return mappings
