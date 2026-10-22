from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5-nano",
    input="Who is gaurav jagtap from avdhootnagr ,nagpur ,maharashtra , india"
)

print(response)