import os

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from google import genai


# Create FastAPI application
app = FastAPI(title="EduGenie")


# Connect static CSS files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# Templates folder
templates = Jinja2Templates(
    directory="templates"
)


# Connect Google Gemini
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# Home page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


# Ask question
@app.post("/ask", response_class=HTMLResponse)
def ask_question(
    request: Request,
    question: str = Form(...)
):

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