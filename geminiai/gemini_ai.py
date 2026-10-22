import requests
from dotenv import load_dotenv
import os

load_dotenv()

response = requests.post(
    "https://generativelanguage.googleapis.com/v1beta/interactions",
    headers={
        "x-goog-api-key": os.getenv("GOOGLE_API_KEY"),
        "Content-Type": "application/json"
    },
    json={
        "model": "gemini-3.5-flash-lite",
        "input": "Which programming language do you use?"
    }
)

data = response.json()
print(data)
