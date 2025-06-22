from openai import AzureOpenAI
from config import AZURE_OPENAI_KEY, AZURE_DEPLOYMENT_NAME, AZURE_ENDPOINT

client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2023-07-01-preview",
    azure_endpoint=AZURE_ENDPOINT
)

def analyze_bias(source_summaries):
    comparison_prompt = (
        "Compare the tone, sentiment, and factual bias of the following news summaries "
        "from different sources. Be neutral in judgment and highlight how each presents the story.\n\n"
    )
    for source, summary in source_summaries.items():
        comparison_prompt += f"{source}:\n{summary}\n\n"

    response = client.chat.completions.create(
        model=AZURE_DEPLOYMENT_NAME,
        messages=[{"role": "user", "content": comparison_prompt}],
        temperature=0.6,
        max_tokens=300
    )
    return response.choices[0].message.content
