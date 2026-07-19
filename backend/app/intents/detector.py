from app.intents.registry import INTENTS


def detect_intent(user_input: str):

    text = user_input.lower()

    if any(word in text for word in ["hi", "hello", "hey"]):
        return INTENTS["greeting"]

    if "youtube" in text:
        return INTENTS["open_youtube"]

    return INTENTS["unknown"]