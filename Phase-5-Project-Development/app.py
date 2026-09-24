import os

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from google import genai

app = FastAPI(title="EduGenie")

templates = Jinja2Templates(directory="Phase-5-Project-Development/templates")

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
def ask_question(request: Request, question: str = Form(...)):

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=question
    )

    answer = response.text

    return templates.TemplateResponse(
        "response.html",
        {
            "request": request,
            "question": question,
            "answer": answer
        }
    )