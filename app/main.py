"""
TaskMesh App Main Module
"""

from fastapi import FastAPI
from app.api.v1.endpoints.health import router as health_router

# Initialize FastAPI Instance
app = FastAPI()


# Attach Health Endpoint to FastAPI Instance
app.include_router(health_router)
