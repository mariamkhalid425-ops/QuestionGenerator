# 🤖 Question Generator 🚀

Ever wanted to create your own super-powered quiz? This app lets you pick a subject and a topic, and then it finds cool questions for you!

## 🛠️ Quick Start
**Open your powershell**
1. Set your API key (get it from https://openrouter.ai/dashboard)
$env:OPENROUTER_API_KEY = "sk-or-v1-YOUR-KEY-HERE"
2.  Enter the folder
cd C:\Users\x\IdeaProjects\QuestionsGenerator
3. **Turn on your Python environment**:
    *   Linux/Mac: `source .venv/bin/activate`
    *   Windows: `.venv\Scripts\activate`
4. **Install the magic tools** (only the first time):
    ```bash
   py -m pip install fastapi uvicorn requests
    ```
5. **Launch the app**:
    ```bash
    py -uvicorn main:app --reload 
    ```
6. **Open your browser** and go to: `http://localhost:8000`

## 🎮 How to Play

1.  **Subject**: Type something like "Science" or "History".
2.  **Topic**: Type something specific like "Space" or "Dinosaurs".
3.  **Count**: Pick how many questions you want.
4.  **Click "Generate"** and watch the magic happen! ✨

## 📂 What's inside?
- `main.py`: The "brain" of our app.
- `static/index.html`: The "face" of our app that you see in the browser.

Future Improvements
-Generate questions with multiple choice options(A, B, C, D)
-Add a question type selector in the form (Theory Question / MCQ)
-Show answer key with explanations
-Save previously generated quizzes to a database for later review
-Add a timed quiz feature where users can answer questions and get scored
-Add a dropdown for difficulty: Easy, Medium, Hard

Built with♥️by Khalid Mariam Wumpaa.

