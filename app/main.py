"""
TaskMesh App Main Module
"""

from fastapi import FastAPI
from app.api.v1.endpoints.router import router as api_router

# Initialize FastAPI Instance
app = FastAPI(
    title="TaskMesh",
    version="1.0",
    docs_url="/docs"
)


# Attach Router Endpoints
app.include_router(api_router)
