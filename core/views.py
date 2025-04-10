from rest_framework.decorators import api_view
from rest_framework.response import Response

from .agents import (
    design_agent,
    source_discovery_agent,
    mapping_agent,
    flow_agent,
    certification_agent
)

# 1. Generate schema from fixed use case
@api_view(['GET'])
def design_schema_view(request):
    schema = design_agent.design_schema()
    return Response({"schema": schema})  # schema must be a list, not a string

# 2. Discover source mappings from schema
@api_view(['POST'])
def source_discovery_view(request):
    schema_fields = request.data.get("schema", [])
    result = source_discovery_agent.find_sources_for_schema_fields(schema_fields)
    return Response({"source_mappings": result})

# 3. Generate transformation mapping
@api_view(['POST'])
def mapping_agent_view(request):
    discovered = request.data.get("source_mappings", [])
    result = mapping_agent.generate_mapping_table(discovered)
    return Response({"mapping_table": result})

# 4. Recommend ingress/egress/storage
@api_view(['GET'])
def flow_agent_view(request):
    result = flow_agent.generate_data_flow_recommendations()
    return Response(result)

# 5. Certification checks
@api_view(['POST'])
def certification_view(request):
    schema = request.data.get("schema", [])
    result = certification_agent.validate_schema(schema)
    return Response(result)
