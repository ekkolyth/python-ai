import os
from dotenv import load_dotenv
from google import genai

# --- Load environment variables ---
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# --- Setup Gemini client ---
client = genai.Client(api_key=api_key)
model = "gemini-2.5-flash"


# --- Function to send prompts ---
def chatGen(model_name, user_prompt):
    chat_response = client.models.generate_content(
        model=model_name,
        contents=user_prompt
    )
    return chat_response


# --- Main interactive loop ---
print("Gemini CLI Chat — type 'exit' to quit.\n")

while True:
    prompt = input("You: ")

    if prompt.strip().lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    if not prompt.strip():
        continue  # skip empty input

    try:
        chat_response = chatGen(model, prompt)
        print("\nGemini:", chat_response.text, "\n")
    except Exception as e:
        print(f"Error: {e}\n")
