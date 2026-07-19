from app.brain.thinking import analyze


class Brain:

    def process_request(self, user_input: str):
        return analyze(user_input)