import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load configuration from environment variables with fallbacks
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY", "4UNE72TyqkDkxWlTLjnYhm9vFR7UIL1EZoRURtPVtumGQmxBeA7NJQQJ99BFACHYHv6XJ3w3AAAAACOGinB8")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT", "https://yaswa-mc6gt1gv-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-4-autodev/chat/completions?api-version=2025-01-01-preview")
AZURE_WEB_APP_NAME = os.getenv("AZURE_WEB_APP_NAME", "testinkey")
AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME", "gpt-4-autodev")
SERPAPI_KEY = os.getenv("SERPAPI_KEY", "eaa6686354c7b6f58c8bcdfac4d9b41aef98e68e5ad4f94c363315c211bd9590")
