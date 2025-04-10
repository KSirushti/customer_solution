import requests
import json
import re

OLLAMA_URL = "http://localhost:11434/api/chat"

def design_schema():
    prompt = """
You are a data product schema designer.

Business Use Case:
"Early Detection of High-Risk Yet Valuable Customers for Proactive Retention and Upsell"

Design a target schema with field names and data types.
Return JSON only in the format:
[
  {"field": "customer_id", "type": "string"},
  {"field": "credit_score", "type": "float"},
  ...
]
"""

    response = requests.post(OLLAMA_URL, json={
        "model": "mistral",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    })

    content = response.json().get("message", {}).get("content", "")

    # Extract just the JSON part inside ```json ... ```
    match = re.search(r"```json\n(.*?)```", content, re.DOTALL)
    if match:
        json_str = match.group(1)
    else:
        json_str = content  # fallback

    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        return [{"error": "Could not parse schema JSON"}]
