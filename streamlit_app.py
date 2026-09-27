import streamlit as st
import os
from google import genai

st.set_page_config(page_title="EduGenie")

st.title("EduGenie")
st.subheader("Google Gemini Powered Learning Assistant")
st.write("Learn - Understand - Explore")

task = st.selectbox(
    "Choose a Task",
    ["Q&A", "Explain", "Quiz", "Summary", "Learning Path"]
)

question = st.text_area(
    "Enter your topic, question or text",
    height=150
)

if st.button("Ask EduGenie"):

    api_key = os.getenv("GEMINI_API_KEY")

    if api_key:

        client = genai.Client(api_key=api_key)

        prompts = {
            "Q&A": "Answer this student's question clearly and simply:\n",
            "Explain": "Explain this topic in very simple words for a student:\n",
            "Quiz": "Create 3 simple multiple-choice questions with 4 options and answers about:\n",
            "Summary": "Summarize this text in simple points:\n",
            "Learning Path": "Create a beginner, intermediate and advanced learning path for:\n"
        }

        prompt = prompts[task] + question

        try:

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

            st.subheader("EduGenie Response")
            st.write(response.text)

        except Exception as e:

            st.error(str(e))

    else:

        st.error("Gemini API key is not configured.")