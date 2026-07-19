from app.intents.detector import detect_intent
from app.planner.planner import create_plan
from app.planner.executor import execute


def analyze(user_input: str):

    intent = detect_intent(user_input)

    plan = create_plan(
        intent.name,
        user_input
    )

    execution = execute(plan)

    if intent.name == "greeting":

        return {
            "intent": intent.name,
            "tool": intent.tool,
            "plan": execution,
            "response": "Hello Vaibhav. Systems Online."
        }

    if intent.name == "open_youtube":

        return {
            "intent": intent.name,
            "tool": intent.tool,
            "plan": execution,
            "response": "Planning complete."
        }

    return {
        "intent": intent.name,
        "tool": intent.tool,
        "plan": execution,
        "response": "Unknown request."
    }