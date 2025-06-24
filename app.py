from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import asyncio
from utils.serpapi_fetcher import get_articles_serpapi
from utils.generic_scraper import scrape_article_text
from utils.summarizer import summarize_articles
from utils.bias_analyzer import analyze_bias
from utils.async_processor import fetch_and_scrape_articles_async

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET", "POST"])
def index():
    comparison_result = summaries = {}
    topic = ""
    error = None
    if request.method == "POST":
        try:
            topic = request.form["topic"]
            sources = {
                "CNN": "cnn.com",
                "Fox News": "foxnews.com"
            }
            articles = asyncio.run(fetch_and_scrape_articles_async(topic, sources))
            summaries = summarize_articles(articles)
            comparison_result = analyze_bias(summaries)
        except Exception as e:
            error = str(e)
    return render_template("index.html", summaries=summaries, result=comparison_result, topic=topic, error=error)

@app.route("/api/analyze", methods=["POST"])
def analyze_news():
    try:
        data = request.get_json()
        topic = data.get("topic", "")
        if not topic:
            return jsonify({"error": "Topic is required"}), 400

        sources = {
            "CNN": "cnn.com",
            "Fox News": "foxnews.com"
        }
        articles_data = asyncio.run(fetch_and_scrape_articles_async(topic, sources))
        # articles_data: {source: {"articles": [...], "links": [...]}}
        summaries = summarize_articles({k: v["articles"] for k, v in articles_data.items()})
        comparison_result = analyze_bias(summaries)
        # Prepare links for frontend
        source_links = {k: v["links"] for k, v in articles_data.items()}
        return jsonify({
            "topic": topic,
            "summaries": summaries,
            "bias_analysis": comparison_result,
            "source_links": source_links
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
