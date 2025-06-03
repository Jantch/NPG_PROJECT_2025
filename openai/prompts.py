from openai import OpenAI


class Prompt:
    def __init__(self, model: str):
        self.model = model
        self.response = None
        self.client = OpenAI(
            api_key="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"
        )

    def create_prompt(self, store: bool, message: str):
        self.response = self.client.responses.create(
            model=self.model,
            input=message
        )
    def get_response(self):
        if self.response != None:
            return self.response.output_text
