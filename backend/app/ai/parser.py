import json


def parse_response(response: str):

    try:
        return json.loads(response)

    except Exception:

        return {
            "intent": "unknown",
            "tool": None,
            "plan": [],
            "response": response
        }