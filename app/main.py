"""
TaskMesh App Main Module
"""

from fastapi import FastAPI
from app.api.v1.router import router as api_router
from app.core.config import settings
from app.core.lifecycle import lifespan

# Initialize FastAPI Instance
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    docs_url="/docs",
    lifespan=lifespan
)


# Attach Router Endpoints
app.include_router(api_router)
