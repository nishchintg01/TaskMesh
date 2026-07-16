"""
Health Endpoint Response Module
"""
from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
