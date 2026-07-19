from app.intents.models import Intent


INTENTS = {
    "greeting": Intent(
        name="greeting",
        tool=None,
        confidence=1.0,
    ),

    "open_youtube": Intent(
        name="open_youtube",
        tool="browser",
        confidence=1.0,
    ),

    "unknown": Intent(
        name="unknown",
        tool=None,
        confidence=0.0,
    ),
}