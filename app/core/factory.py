"""
Factory Module to Initilize FastAPI Instance
"""
from fastapi import FastAPI
from app.api.v1.router import router as api_router
from app.core.config import settings
from app.core.lifecycle import lifespan

def create_app():
    """
    Function to Initialize FastAPI App Instance
    """

    # Initialize FastAPI Instance
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        docs_url="/docs",
        lifespan=lifespan,
    )

    # Attach Router Endpoints
    app.include_router(api_router)
    return app
