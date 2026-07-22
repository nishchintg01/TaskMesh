"""
    Request Id Module
"""
from typing import Callable, Awaitable
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response
from app.core.logger import Logger


logger = Logger(__name__)

class LoggingMiddleware(BaseHTTPMiddleware):
    """
    FastAPI Middleware to Generate Request Logs
    for Incoming Http Requests

    Args:
        BaseHTTPMiddleware (BaseHTTPMiddleware): Inherits starlette basehttpMiddleware
    """
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        """
        Function to Generate Request Logs

        Args:
            request (Request): Incoming Http Request Data
            call_next (Callable[[Request], Awaitable[Response]]): path function which takes 
                                                request as argument and returns path response

        Returns:
            Response: Request Reponse
        """
        response = await call_next(request)
        logger_info = {
            "method" : request.scope["method"],
            "path" : request.scope["path"],
            "status": response.status_code,
            "duration" : request.state["duration"],
            "request_id": request.state["request_id"]
        }
        logger.info(f"Request Info : {logger_info}")
        return response
