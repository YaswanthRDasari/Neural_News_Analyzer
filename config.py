import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load configuration from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

# Validate required environment variables
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is required")
if not OPENAI_MODEL:
    raise ValueError("OPENAI_MODEL environment variable is required")
if not SERPAPI_KEY:
    raise ValueError("SERPAPI_KEY environment variable is required")
