import aiohttp
import asyncio
from config import SERPAPI_KEY

async def get_articles_serpapi_async(topic, site_filter, max_results=3):
    params = {
        "q": f"{topic} site:{site_filter}",
        "api_key": SERPAPI_KEY,
        "engine": "google",
        "num": max_results
    }

    async with aiohttp.ClientSession() as session:
        async with session.get("https://serpapi.com/search", params=params) as response:
            results = await response.json()

    links = []
    for res in results.get("organic_results", []):
        link = res.get("link")
        if link:
            links.append(link)
    print(f"[{site_filter}] Links found:", links)
    return links

# Keep the original sync function for backward compatibility
def get_articles_serpapi(topic, site_filter, max_results=3):
    return asyncio.run(get_articles_serpapi_async(topic, site_filter, max_results))
