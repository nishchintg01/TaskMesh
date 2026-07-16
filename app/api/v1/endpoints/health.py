"""
FastAPI Health Routing Module
"""
from fastapi import APIRouter
from app.schemas.health.response import HealthResponse


router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/", response_model = HealthResponse)
async def health():
    """Function to return APP Health

    Returns:
        dict: returns tashMesh App Health Info
    """
    return {"status": "healthy", "service": "TaskMesh", "version": "0.1.0"}
