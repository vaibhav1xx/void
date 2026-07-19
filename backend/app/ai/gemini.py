import os

from dotenv import load_dotenv
from google import genai

from app.ai.prompts import SYSTEM_PROMPT


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(user_input: str):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            SYSTEM_PROMPT,
            user_input
        ]
    )

    return response.text