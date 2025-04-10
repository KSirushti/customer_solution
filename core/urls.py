from django.urls import path
from . import views

urlpatterns = [
    path('schema/', views.design_schema_view),
    path('discover/', views.source_discovery_view),
    path('mapping/', views.mapping_agent_view),
    path('flows/', views.flow_agent_view),
    path('certify/', views.certification_view),
]
