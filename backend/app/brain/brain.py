from app.ai.provider import generate


class Brain:

    def process_request(self, user_input: str):

        return generate(user_input)