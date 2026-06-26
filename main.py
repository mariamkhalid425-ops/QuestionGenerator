import json
import os
import requests
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# OpenRouter API configuration
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def build_page(results_html=""):
    with open("static/index.html") as file:
        html = file.read()

    # put the results where the placeholder is
    html = html.replace("<!-- RESULTS -->", results_html)

    return html

@app.get("/")
def home():
    return HTMLResponse(build_page())

@app.post("/generate")
def generate(
    subject: str = Form(), 
    topic: str = Form(), 
    num_questions: int = Form(),
):
    
    intructions = (
        f"Generate exactly {num_questions} questions about the topic "
        f'"{topic}" in the subject "{subject}". '
        f"Return ONLY a JSON array of strings, no other text. "
        f'Example: ["Question 1?", "Question 2?"]'
    )

    try:
        response = requests.post(
            url=OPENROUTER_URL,
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "HTTP-Referer": "http://localhost:8000",
                "X-Title": "Question Generator",
            },
            json={
                "model": "meta-llama/llama-3.3-70b-instruct",
                "messages": [{"role": "user", "content": intructions}],
            },
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        response_text = data["choices"][0]["message"]["content"]
    except Exception as e:
        error_html = f"""
        <div class="results error">
            <h2>Error</h2>
            <p>Failed to generate questions. Please try again.</p>
            <p><small>Error: {str(e)}</small></p>
        </div>
        """
        return HTMLResponse(build_page(error_html))

    # parse the questions from the API response
    try:
        questions = json.loads(response_text)
        # ensure questions is a list
        if not isinstance(questions, list):
            questions = [questions]
    except:
        questions = [q.strip() for q in response_text.split("\n") if q.strip()]

    # build the results list
    if not questions:
        error_html = """
        <div class="results error">
            <h2>No Questions Generated</h2>
            <p>Could not generate questions. Please try again with different parameters.</p>
        </div>
        """
        return HTMLResponse(build_page(error_html))

    questions_html = ""
    for question in questions:
        question = str(question).strip()
        if question:
            questions_html = questions_html + f"<li>{question}</li>"

    results_html = f"""
       <div class="results">
           <h2>{subject} - {topic}</h2>
           <ol>{questions_html}</ol>
       </div>
       """

    return HTMLResponse(build_page(results_html))

