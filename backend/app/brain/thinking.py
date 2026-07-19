def analyze(user_input: str):
    text = user_input.lower()

    if any(word in text for word in ["hi", "hello", "hey"]):
        return {
            "intent": "greeting",
            "plan": [],
            "tool": None,
            "response": "Hello Vaibhav. Systems Online."
        }

    if "youtube" in text:
        return {
            "intent": "open_youtube",
            "plan": [
                "Open browser",
                "Navigate to YouTube"
            ],
            "tool": "browser",
            "response": "Planning to open YouTube."
        }

    return {
        "intent": "unknown",
        "plan": [],
        "tool": None,
        "response": "I don't understand the request yet."
    }