import logging
import os
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

# Setup Logging
def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

setup_logging()
load_dotenv()

# Load GPT-2 Model
def load_gpt2_model():
    model_name = "gpt2"
    logging.info("Loading GPT-2 model...")
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=128, device_map="auto")
        logging.info("Model loaded successfully.")
        return pipe
    except Exception as e:
        logging.error(f"Error loading model: {e}")
        exit(1)

llm = load_gpt2_model()

# Split Text
def split_text_into_chunks(text, max_tokens=128):
    tokens = text.split()
    return [" ".join(tokens[i:i + max_tokens]) for i in range(0, len(tokens), max_tokens)]

# Define Agents
class ResearchAgent:
    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY")

    def find_trending_topics(self):
        response = requests.get(f"https://newsapi.org/v2/top-headlines?category=business&apiKey={self.api_key}")
        data = response.json()
        return [article['title'] for article in data.get("articles", [])]

    def collect_information(self, topic):
        response = requests.get(f"https://newsapi.org/v2/everything?q={topic}&apiKey={self.api_key}")
        data = response.json()
        return [article['description'] for article in data.get("articles", [])]

class ContentPlanningAgent:
    def create_outline(self, topic, research_data):
        prompt = f"Create a blog outline on {topic} using: {research_data}"
        return llm(prompt, max_new_tokens=128)[0]['generated_text']

class ContentGenerationAgent:
    def generate_content(self, outline):
        chunks = split_text_into_chunks(outline)
        generated_content = []
        for chunk in chunks:
            prompt = f"Write blog content based on: {chunk}"
            generated_chunk = llm(prompt, max_new_tokens=128)[0]['generated_text']
            generated_content.append(generated_chunk)
        return " ".join(generated_content)

class SEOOptimizationAgent:
    def optimize_content(self, content, keywords):
        chunks = split_text_into_chunks(content)
        optimized_content = []
        for chunk in chunks:
            prompt = f"Optimize for SEO with keywords {keywords}: {chunk}"
            optimized_chunk = llm(prompt, max_new_tokens=128)[0]['generated_text']
            optimized_content.append(optimized_chunk)
        return " ".join(optimized_content)

class ReviewAgent:
    def review_content(self, content):
        chunks = split_text_into_chunks(content)
        reviewed_content = []
        for chunk in chunks:
            prompt = f"{chunk}"
            reviewed_chunk = llm(prompt, max_new_tokens=128)[0]['generated_text']
            reviewed_content.append(reviewed_chunk)
        return " ".join(reviewed_content)

# Initialize Flask App
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Route to Generate Blog
@app.route('/generate', methods=['POST'])
def generate_blog():
    data = request.json
    keywords = data.get('keywords', [])
    
    # Instantiate Agents
    research_agent = ResearchAgent()
    topic = research_agent.find_trending_topics()[0]
    research_data = research_agent.collect_information(topic)

    planning_agent = ContentPlanningAgent()
    outline = planning_agent.create_outline(topic, research_data)

    generation_agent = ContentGenerationAgent()
    content = generation_agent.generate_content(outline)

    seo_agent = SEOOptimizationAgent()
    optimized_content = seo_agent.optimize_content(content, keywords)

    review_agent = ReviewAgent()
    final_content = review_agent.review_content(optimized_content)

    # Save to File
    with open("final_blog_post.txt", "w", encoding="utf-8") as file:
        file.write(final_content)

    return jsonify({'content': final_content})

# Run the Flask App
if __name__ == "__main__":
    app.run(debug=True)
