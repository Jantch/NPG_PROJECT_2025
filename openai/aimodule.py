from prompts import Prompt
from speechtransition import text_to_speech
import random

class Hint:
    def __init__(self):
        self.riddles_with_prompts = {"kółko i krzyżyk": "stwórz zagadkę jednozdaniową która zasugeruje aby wygrać w kółko i krzyżyk aby przejść dalej"
                                 ,"układanie klocków":"stwórz zagadkę jednozdaniową, która zasugeruje aby ulozyc klocki na planszy w odpowiedniej kolejnosci zgodnie z ustawieniem kolorów ksiażek na półce, w sposób nieoczywisty"}
    def get_hint(self, zagadki_rozwiazane: list) -> str:
        prompt = Prompt("gpt-4.1")
        riddles_not_finished = []
        for riddle in self.riddles_with_prompts.keys():
            if riddle not in zagadki_rozwiazane:
                riddles_not_finished.append(self.riddles_with_prompts[riddle])
        random_choice = random.choice(riddles_not_finished)
        prompt.create_prompt(store=False, message=random_choice)
        return text_to_speech(text=prompt.get_response())

if __name__ == "__main__":
    hint = Hint()
    hint.get_hint(["kółko i krzyżyk"])