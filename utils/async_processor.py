import asyncio
from .serpapi_fetcher import get_articles_serpapi_async
from .generic_scraper import scrape_article_text_async

def flatten_and_filter(lst):
    return [x for x in lst if isinstance(x, str) and x.strip()]

async def fetch_and_scrape_articles_async(topic, sources):
    """
    Fetch articles from multiple sources concurrently and scrape their content.
    
    Args:
        topic (str): The topic to search for
        sources (dict): Dictionary mapping source names to domain filters
                       e.g., {"CNN": "cnn.com", "Fox News": "foxnews.com"}
    
    Returns:
        dict: {source: {"articles": [scraped_texts], "links": [urls]}}
    """
    articles = {}
    
    # Fetch URLs from all sources concurrently
    url_tasks = {
        source: get_articles_serpapi_async(topic, domain)
        for source, domain in sources.items()
    }
    
    url_results = await asyncio.gather(*url_tasks.values(), return_exceptions=True)
    
    # Create a mapping of source names to their URL results
    source_urls = dict(zip(sources.keys(), url_results))
    
    # Scrape articles from all sources concurrently
    scrape_tasks = {}
    for source, urls in source_urls.items():
        if isinstance(urls, Exception):
            print(f"Error fetching URLs for {source}: {urls}")
            articles[source] = {"articles": [], "links": []}
            continue
            
        # Create tasks for scraping each URL from this source
        source_tasks = [scrape_article_text_async(url) for url in urls]
        scrape_tasks[source] = asyncio.gather(*source_tasks, return_exceptions=True)
    
    # Execute all scraping tasks concurrently
    if scrape_tasks:
        scrape_results = await asyncio.gather(*scrape_tasks.values(), return_exceptions=True)
        
        # Process results
        for source, result in zip(scrape_tasks.keys(), scrape_results):
            if isinstance(result, Exception):
                print(f"Error scraping articles for {source}: {result}")
                articles[source] = {
                    "articles": [],
                    "links": source_urls.get(source, [])
                }
            else:
                articles[source] = {
                    "articles": flatten_and_filter(result),
                    "links": source_urls.get(source, [])
                }
    else:
        for source in sources.keys():
            if source not in articles:
                articles[source] = {"articles": [], "links": source_urls.get(source, [])}
    
    return articles 