from fastapi import APIRouter
from uuid import uuid4
import asyncio
from app.schemas.response import UUIDResponse, CatResponse
from app.services.v1.cat_service import fetch_cat_image
import logging
from app.middleware.logger import logger

router = APIRouter()

@router.get("/uuid", response_model=UUIDResponse)
async def get_uuid():
    # Generate and return a random UUID (version 4)
    new_uuid = str(uuid4())
    logger.info(f"Generated UUID: {new_uuid}")
    return UUIDResponse(uuid=new_uuid)

@router.get("/async-uuid", response_model=UUIDResponse)
async def get_async_uuid():
    # Generate a UUID (version 4) after a 3-second delay
    logger.info("Starting async UUID generation with a 3-second delay")
    await asyncio.sleep(3)
    new_uuid = str(uuid4())
    logger.info(f"UUID generated after delay: {new_uuid}")
    return UUIDResponse(uuid=new_uuid)

@router.get("/cat", response_model=CatResponse)
async def get_cat_image():
    # Fetch and return a random cat image URL from the service
    logger.info("Fetching cat image from service")
    image_url = await fetch_cat_image()
    logger.info(f"Fetched cat image URL: {image_url}")
    return CatResponse(cat_image_url=image_url)
