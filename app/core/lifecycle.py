"""
FastAPI Lifespan Context Manager Module
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.logger import Logger


logger = Logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    FastAPI LifeSpan Function 

    Args:
        app (FastAPI): Accepts FastAPI Object as Arguments
    """
    logger.info("TaskMesh Application is starting...")
    yield
    logger.info("TaskMesh Application is Shutting Down...")
