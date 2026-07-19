from app.planner.task import Task


def create_plan(intent_name: str, user_input: str):

    tasks = []

    text = user_input.lower()

    if intent_name == "greeting":
        return tasks

    if intent_name == "open_youtube":

        tasks.append(
            Task(
                action="open_browser",
                target="YouTube"
            )
        )

        if "search" in text:

            query = text.split("search", 1)[1].strip()

            tasks.append(
                Task(
                    action="search",
                    target=query
                )
            )

        return tasks

    return tasks