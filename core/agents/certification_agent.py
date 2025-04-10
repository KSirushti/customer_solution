def validate_schema(schema):
    issues = []

    for field in schema:
        name = field["field"]
        dtype = field["type"]

        if not name.islower():
            issues.append(f"Field '{name}' should be lowercase.")
        if " " in name:
            issues.append(f"Field '{name}' should not contain spaces.")
        if dtype not in ["string", "float", "integer", "date", "boolean", "datetime"]:
            issues.append(f"Unsupported type '{dtype}' for field '{name}'.")

    return {
        "status": "PASS" if not issues else "FAIL",
        "issues": issues
    }
