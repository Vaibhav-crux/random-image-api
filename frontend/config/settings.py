from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch API base URL from environment, with a default fallback
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000/v1")