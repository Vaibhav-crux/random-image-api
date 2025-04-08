from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import httpx
import asyncio
import logging
from app.middleware.logger import logger

class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            # Process the incoming request and get the response
            response = await call_next(request)
            return response

        # Handle HTTP errors from external services (like cataas.com)
        except httpx.HTTPError as e:
            logger.error(f"HTTP error occurred: {str(e)}")
            return JSONResponse(
                status_code=502,  # Bad Gateway
                content={"detail": f"External service error: {str(e)}"}
            )

        # Handle request timeout errors
        except asyncio.TimeoutError:
            logger.error("Request timed out")
            return JSONResponse(
                status_code=504,  # Gateway Timeout
                content={"detail": "Request timed out"}
            )

        # Handle bad request or invalid data errors
        except ValueError as e:
            logger.error(f"Value error: {str(e)}")
            return JSONResponse(
                status_code=400,  # Bad Request
                content={"detail": f"Bad request: {str(e)}"}
            )

        # Handle unexpected server-side errors
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return JSONResponse(
                status_code=500,  # Internal Server Error
                content={"detail": f"Internal server error: {str(e)}"}
            )

def add_error_handler_middleware(app):
    # Register the custom error handler middleware in the FastAPI app
     app.add_middleware(ErrorHandlerMiddleware)
