from openai import OpenAI


class Prompt:
    def __init__(self, model: str):
        self.model = model
        self.response = None
        self.client = OpenAI(
            api_key="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")

    def create_prompt(self, store: bool, message: str):
        self.response = self.client.responses.create(
            model=self.model,
            input=message
        )
    def get_response(self):
        if self.response != None:
            return self.response.output_text
