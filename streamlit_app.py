import streamlit as st
import os
from google import genai

st.set_page_config(
    page_title="EduGenie",
    page_icon="🎓"
)

st.title("🎓 EduGenie")
st.subheader("Google Gemini Powered Learning Assistant")
st.write("Learn - Understand - Explore")

task = st.selectbox(
    "Choose a Task:",
    [
        "Q&A",
        "Explain",
        "Quiz",
        "Summary",
        "Learning Path"
    ]
)

question = st.text_area(
    "Enter your topic, question or text:",
    height=150
)

if st.button("Ask EduGenie"):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        st.error("Gemini API key is not configured.")

    else:
        client = genai.Client(api_key=api_key)

        if task == "Q&A":
            prompt = f"Answer this student's question clearly and simply:\n{question}"

        elif task == "Explain":
            prompt = f"Explain this topic in very simple words for a student:\n{question}"

        elif task == "Quiz":
           