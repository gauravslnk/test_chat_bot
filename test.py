import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")

model = genai.GenerativeModel("gemini-1.5-flash")

def chat_with_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {e}"

if __name__ == "__main__":

    print("\n Chat with Gemini (type 'exit' to quit):")
    while True:
        user_input = input("\n You: ")
        if user_input.lower() in ["exit", "quit", "q"]:
            print("\n Exiting the chat. Goodbye!")
            break
        response = chat_with_gemini(user_input)
        print(f"\n Gemini: {response}")
