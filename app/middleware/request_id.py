"""
    Request Id Module
"""
import uuid
from typing import Callable, Awaitable
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response


class RequestIdMiddleware(BaseHTTPMiddleware):
    """
    FastAPI Middleware to Generate Request ID
    for Incoming Http Requests

    Args:
        BaseHTTPMiddleware (BaseHTTPMiddleware): Inherits starlette basehttpMiddleware
    """
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        """
        Function to Generate Request ID

        Args:
            request (Request): Incoming Http Request Data
            call_next (Callable[[Request], Awaitable[Response]]): path function which takes 
                                                request as argument and returns path response

        Returns:
            Response: Request Reponse
        """
        request_id = str(uuid.uuid4())
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        request.state["request_id"] = request_id
        return response
