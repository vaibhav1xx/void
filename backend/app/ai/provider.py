from app.ai.gemini import ask_gemini
from app.ai.parser import parse_response


def generate(user_input: str):

    raw = ask_gemini(user_input)

    parsed = parse_response(raw)

    return parsed