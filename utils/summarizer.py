from openai import AzureOpenAI
from config import AZURE_OPENAI_KEY, AZURE_DEPLOYMENT_NAME, AZURE_ENDPOINT

client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2023-07-01-preview",
    azure_endpoint=AZURE_ENDPOINT
)

def summarize_articles(articles_dict):
    summaries = {}
    for source, articles in articles_dict.items():
        joined_articles = " ".join([a for a in articles if a])
        if not joined_articles:
            continue
        prompt = f"Summarize the following text in 3 bullet points:\n{joined_articles}"
        response = client.chat.completions.create(
            model=AZURE_DEPLOYMENT_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=250
        )
        summaries[source] = response.choices[0].message.content
    return summaries
