from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def summarize_articles(articles_dict):
    summaries = {}
    for source, articles in articles_dict.items():
        joined_articles = " ".join([a for a in articles if a])
        if not joined_articles:
            continue
        prompt = f"Summarize the following text in 3 bullet points:\n{joined_articles}"
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=250
        )
        summaries[source] = response.choices[0].message.content
    return summaries
