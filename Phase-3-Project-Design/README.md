# Phase 3 – Project Design

## Project Name
EduGenie – Google Gemini Powered Learning Assistant

## System Architecture

Student
   ↓
Web Interface
   ↓
FastAPI Backend
   ↓
Google Gemini AI
   ↓
Generated Response
   ↓
Web Interface
   ↓
Student

## Main Components

1. Frontend – HTML, CSS and JavaScript
2. Backend – FastAPI
3. AI Model – Google Gemini
4. Template Engine – Jinja2
5. Server – Uvicorn

## Working Flow

1. Student enters a question.
2. FastAPI receives the question.
3. The question is sent to Gemini AI.
4. Gemini generates the answer.
5. The answer is returned to the application.
6. EduGenie displays the answer to the student.