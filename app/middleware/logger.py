import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

# Configure the default logging settings
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create a logger instance for this module
logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Log the incoming request method and URL
        logger.info(f"Request: {request.method} {request.url}")

        # Process the request and get the response
        response = await call_next(request)

        # Log the response status code
        logger.info(f"Response: {response.status_code}")

        return response

def add_logging_middleware(app):
    # Register the logging middleware in the FastAPI app
    app.add_middleware(LoggingMiddleware)
