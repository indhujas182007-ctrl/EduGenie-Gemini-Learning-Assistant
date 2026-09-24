import os

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from google import genai


app = FastAPI(title="EduGenie")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(
    directory="templates"
)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


@app.post("/ask", response_class=HTMLResponse)
def ask_question(
    request: Request,
    task: str = Form(...),
    question: str = Form(...)
):

    if task == "qa":
        prompt = f"Answer this academic question clearly and simply:\n{question}"

    elif task == "explain":
        prompt = f"Explain this topic in simple words for a student:\n{question}"

    elif task == "quiz":
        prompt = f"""
Create 3 multiple-choice questions about this topic.

Topic:
{question}

Give 4 options for each question and clearly mention the correct answer.
"""

    elif task == "summary":
        prompt = f"Summarize the following text in simple words:\n{question}"

    elif task == "learning_path":
        prompt = f"""
Create a beginner-to-advanced learning path