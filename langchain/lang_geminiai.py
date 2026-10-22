from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

response = model.invoke("Hello, how is indian prime minister?")

print(response.content)