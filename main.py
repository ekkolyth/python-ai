import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
model = "gemini-2.5-flash"
prompt = input("Enter your prompt: ")


def chatGen(model, prompt):
    chatResponse = client.models.generate_content(
        model=model,
        contents=prompt
    )
    return chatResponse


chatResponse = chatGen(model, prompt)

print("\nModel response:")
print(chatResponse.text)
