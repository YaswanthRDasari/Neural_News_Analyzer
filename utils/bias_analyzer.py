from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def analyze_bias(source_summaries):
    comparison_prompt = (
        "Compare the tone, sentiment, and factual bias of the following news summaries "
        "from different sources. Be neutral in judgment and highlight how each presents the story.\n\n"
    )
    for source, summary in source_summaries.items():
        comparison_prompt += f"{source}:\n{summary}\n\n"

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": comparison_prompt}],
        temperature=0.6,
        max_tokens=300
    )
    return response.choices[0].message.content
