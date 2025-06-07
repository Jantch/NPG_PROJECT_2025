
from gtts import gTTS

import os
def text_to_speech(text: str) -> str:
    # Ścieżka do folderu tego pliku (czyli openaimodule)
    base_path = os.path.dirname(__file__)

    # Pełna ścieżka do folderu hints_voc
    hints_folder = os.path.join(base_path, "hints_voc")
    os.makedirs(hints_folder, exist_ok=True)

    # Pełna ścieżka do pliku
    filename = os.path.join(hints_folder, "sound_of_assistant.wav")

    # Tworzenie dźwięku
    tts = gTTS(text, lang="pl")
    tts.save(filename)

    return filename
