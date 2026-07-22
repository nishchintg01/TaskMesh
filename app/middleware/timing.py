"""
    Timing Module
"""
from time import perf_counter
from typing import Callable, Awaitable
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response


class TimingMiddleware(BaseHTTPMiddleware):
    """
    FastAPI Middleware to Generate Timing
    for Incoming Http Requests

    Args:
        BaseHTTPMiddleware (BaseHTTPMiddleware): Inherits starlette basehttpMiddleware
    """
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        """
        Function to Generate Timing

        Args:
            request (Request): Incoming Http Request Data
            call_next (Callable[[Request], Awaitable[Response]]): path function which takes 
                                                request as argument and returns path response

        Returns:
            Response: Request Reponse
        """
        start_time = perf_counter()
        response = await call_next(request)
        end_time = perf_counter()
        response.headers["X-Process-Time"] = f"{end_time - start_time:.2f}s"
        request.state["duration"] = f"{end_time - start_time:.2f}s"
        return response
