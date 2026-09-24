import os

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from google import genai

app = FastAPI(title="EduGenie")

# Gemini API client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>EduGenie</title>
    </head>
    <body>
        <h1>🎓 EduGenie</h1>
        <h2>Google Gemini Powered Learning Assistant</h2>

        <form action="/ask" method="post">
            <input
                type="text"
                name="question"
                placeholder="Ask your academic question..."
                required
            >
            <button type="submit">Ask EduGenie 🤖</button>
        </form>
    </body>
    </html>
    """


@app.post("/ask", response_class=HTMLResponse)
def ask_question(question: str = Form(...)):

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=question
    )

    answer = response.text

    return f"""
    <html>
    <head>
        <title>EduGenie Response</title>
    </head>
    <body>
        <h1>🎓 EduGenie</h1>

        <h3>📝 Your Question</h3>
        <p>{question}</p>

        <h3>🤖 Gemini AI Response</h3>
        <p>{answer}</p>

        <a href="/">⬅️ Ask another question</a>
    </body>
    </html>
    """