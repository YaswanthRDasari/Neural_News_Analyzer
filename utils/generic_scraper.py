import aiohttp
import asyncio
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

async def scrape_article_text_async(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=HEADERS, timeout=aiohttp.ClientTimeout(total=10)) as response:
                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")
                paragraphs = soup.select("article p") or soup.find_all("p")
                return " ".join(p.get_text() for p in paragraphs[:10])
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return ""

# Keep the original sync function for backward compatibility
def scrape_article_text(url):
    return asyncio.run(scrape_article_text_async(url))
