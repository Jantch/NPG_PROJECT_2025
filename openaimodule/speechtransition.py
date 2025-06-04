import random
from gtts import gTTS

def text_to_speech(text: str, filename: str = f"hints_voc/{random.randint(1, 10000)}.mp3", lang: str = "pl"):
    """
    Konwertuje tekst na mowę i zapisuje jako plik MP3.
    - text: treść do przetworzenia
    - filename: nazwa wyjściowego pliku mp3
    - lang: kod języka (np. "pl" dla polskiego)
    """
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    print(f"Plik dźwiękowy zapisany jako: {filename}")
    return filename


