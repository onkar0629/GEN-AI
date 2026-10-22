
import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

st.title("Gemini AI Interactions")
question = st.text_input("Enter a question")

if st.button("Submit"):
    if question.strip():
        if not api_key:
            st.error("GEMINI_API_KEY is missing from .env file")
        else:
            st.text("You asked: " + question)

            with st.spinner("Generating response..."):
                try:
                    response = requests.post(
                        "https://generativelanguage.googleapis.com/v1beta/interactions",
                        headers={
                            "x-goog-api-key": api_key,
                            "Content-Type": "application/json"
                        },
                        json={
                            "model": "gemini-3.5-flash-lite",
                            "input": question
                        },
                        timeout=30
                    )

                    response.raise_for_status()
                    data = response.json()
                    st.text("Response: " + str(data))

                except requests.exceptions.RequestException as e:
                    st.error(f"API request failed: {e}")
    else:
        st.warning("Please enter a valid question.")
