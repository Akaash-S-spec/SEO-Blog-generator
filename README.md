# Multi-Agent SEO Blog Generator

## Overview

The Multi-Agent SEO Blog Generator is a Flask-based web application designed to automate the process of generating SEO-optimized blog posts. It leverages multiple agents for research, content planning, generation, optimization, and review.

## Features

- Research trending topics using NewsAPI
- Generate blog outlines and content using GPT-2
- Optimize content for SEO with specified keywords
- Review and proofread generated content

## Technologies Used

- Python
- Flask
- Transformers (Hugging Face)
- NewsAPI
- Flask-CORS

## Project Tree Structure

```
C:.
│   .env
│   requirements.txt
│   README.md
├───backend
│       final_blog_post.txt
│       flask_backend.py
│
└───frontend
    │   flask_frontend.py
    │
    ├───static
    │       script.js
    │       style.css
    │
    └───templates
            index.html
```

## Setup Instructions

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install required dependencies using `pip install -r requirements.txt`.
4. Create a `.env` file and add your `NEWS_API_KEY`.
5. Run the Flask backend and frontend.

## Usage

- Send a POST request to `/generate` with keywords to generate a blog.
- The final blog will be saved as `final_blog_post.txt`.

## Future Improvements

- Integrate larger open-source models like Llama 2 and DeepSeek for better and more accurate results.
- Enhance frontend UI for better user interaction.
- Implement a database to store generated blogs for future reference.

## Contributors

- Akaash S



## USE LARGER MODELS LIKE DEEPSEEK OR LLAMA2 ECT.. FOR ACCURATE OUTPUT
