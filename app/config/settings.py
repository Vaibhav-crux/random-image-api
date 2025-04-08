from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch the cat API URL from environment, with a default fallback
CAT_API_URL = os.getenv("CAT_API_URL", "https://cataas.com/cat")