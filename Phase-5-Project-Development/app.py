import os
import json

from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from google import genai

app = FastAPI(title="EduGenie")

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


def ask_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    return response.text


@app.post("/qa")
def qa(question: str = Form(...)):
    return ask_gemini(
        f"Answer this student's question clearly and simply:\n{question}"
    )


@app.post("/explain")
def explain(question: str = Form(...)):
    return ask_gemini(
        f"Explain this topic in very simple words for a student:\n{question}"
    )


@app.post("/quiz")
def quiz(question: str = Form(...)):
    prompt = f"""
Create 3 multiple-choice questions about this topic:

{question}

Each question must have 4 options and the correct answer.
Keep the questions simple for students.
"""
    return ask_gemini(prompt)


@app.post("/summarize")
def summarize(question: str = Form(...)):
    return ask_gemini(
        f"Summarize the following text in simple and short points:\n{question}"
    )


@app.post("/learn/recommendations")
def learning_path(question: str = Form(...)):
    prompt = f"""
Create a learning path for this topic:

{question}

Give:
1. Beginner topics
2. Intermediate topics
3. Advanced topics
4. Suggested learning resources
"""
    return ask_gemini(prompt)


@app.post("/ask", response_class=HTMLResponse)
def ask(
    request: Request,
    task: str = Form(...),
    question: str = Form(...)
):

    if task == "qa":
        answer = qa(question)

    elif task == "explain":
        answer = explain(question)

    elif task == "quiz":
        answer = quiz(question)

    elif task == "summary":
        answer = summarize(question)

    elif task == "learning_path":
        answer = learning_path(question)

    else:
        answer = "Please select a valid task."

    return templates.TemplateResponse(
        "response.html",
        {
            "request": request,
            "question": question,
            "answer": answer
        }
    )