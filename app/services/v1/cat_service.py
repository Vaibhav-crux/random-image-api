import httpx
import logging
from app.middleware.logger import logger
import time
from app.config.settings import CAT_API_URL

async def fetch_cat_image() -> str:
    '''Fetch a random cat image URL from the configured external API
    Uses async HTTP request and handles possible errors'''

    # Add a timestamp query param to avoid cached responses
    url = f"{CAT_API_URL}?ts={int(time.time())}"
    logger.info(f"Fetching cat image from {url}")

    async with httpx.AsyncClient() as client:
        # Send GET request with redirects enabled
        response = await client.get(url, follow_redirects=True)

        # Raise error if the response status is not 200 (OK)
        if response.status_code != 200:
            logger.error(f"Got bad response: {response.status_code}")
            raise httpx.HTTPStatusError(
                message=f"Failed to fetch cat image, status: {response.status_code}",
                request=response.request,
                response=response
            )

        # Extract the final URL after redirects
        final_url = str(response.url)
        logger.info(f"Successfully fetched cat image URL: {final_url}")

        # Return the image URL
        return final_url
