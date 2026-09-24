import os
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from google import genai

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/ask", response_class=HTMLResponse)
def ask(
    request: Request,
    task: str = Form(...),
    question: str = Form(...)
):

    prompt = f"""
You are EduGenie, a learning assistant.

Task: {task}

Student question:
{question}

Give a simple and clear answer for a student.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return templates.TemplateResponse(
        "response.html",
        {
            "request": request,
            "question": question,
            "answer": response.text
        }
    )