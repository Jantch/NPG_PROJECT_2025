from openai import OpenAI
from .config import API_KEY

class Prompt:
    def __init__(self, model: str):
        self.model = model
        self.response = None
        self.client = OpenAI(
            api_key = API_KEY,)
    def create_prompt(self, store: bool, message: str):
        self.response = self.client.responses.create(
            model=self.model,
            input=message
        )
    def get_response(self):
        if self.response != None:
            return self.response.output_text
