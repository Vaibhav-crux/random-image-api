from fastapi import FastAPI
from app.api.v1.routes import router as v1_router
from app.middleware.cors import add_cors_middleware
from app.middleware.error_handler import add_error_handler_middleware
from app.middleware.gzip import add_gzip_middleware
from app.middleware.logger import add_logging_middleware
from app.middleware.rate_limit import add_rate_limit_middleware
from app.middleware.timeout import add_timeout_middleware

app = FastAPI(
    title="FastAPI UUID & Cat API",
    description="A server providing UUID generation and random cat images",
    version="0.1.0"
)

# Add all our middleware
add_timeout_middleware(app)
add_rate_limit_middleware(app)
add_logging_middleware(app)
add_gzip_middleware(app)
add_error_handler_middleware(app)  # Catches any unhandled errors
add_cors_middleware(app)

app.include_router(v1_router, prefix="/v1", tags=["v1"])

@ app.get("/")
async def root():
    """Says hi from the root endpoint."""
    return {"message": "Welcome to the FastAPI UUID & Cat API"}