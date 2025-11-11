from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

def gemini_resp(prompt: str, model: str = "gemini-2.5-flash") -> str:
    """
    Sends a prompt to the Google Gemini model and returns the response text.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("❌ GOOGLE_API_KEY not found. Make sure it's set in your .env file.")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )

    return getattr(response, "text", str(response))


# # testing
# if __name__ == "__main__":
#     answer = gemini_resp("Capital of India?")
#     print(answer)
