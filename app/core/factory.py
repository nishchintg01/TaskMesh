"""
Factory Module to Initilize FastAPI Instance
"""
from fastapi import FastAPI
from app.api.v1.router import router as api_router
from app.core.config import settings
from app.core.lifecycle import lifespan
from app.middleware.request_id import RequestIdMiddleware
from app.middleware.timing import TimingMiddleware
from app.middleware.logging import LoggingMiddleware

def create_app() -> FastAPI:
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

    # Attach Middlewares
    app.add_middleware(RequestIdMiddleware)
    app.add_middleware(TimingMiddleware)
    app.add_middleware(LoggingMiddleware)

    # Attach Router Endpoints
    app.include_router(api_router)
    return app
