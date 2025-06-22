import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load configuration from environment variables
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_WEB_APP_NAME = os.getenv("AZURE_WEB_APP_NAME")
AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

# Validate required environment variables
if not AZURE_OPENAI_KEY:
    raise ValueError("AZURE_OPENAI_KEY environment variable is required")
if not AZURE_ENDPOINT:
    raise ValueError("AZURE_ENDPOINT environment variable is required")
if not SERPAPI_KEY:
    raise ValueError("SERPAPI_KEY environment variable is required")
