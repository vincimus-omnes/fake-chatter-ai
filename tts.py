from gtts import gTTS
from playsound import playsound

def convert_text_and_play(text_to_convert):
    language = 'en'
    file_name = "recording1.mp3"
    speech = gTTS(text=text_to_convert, lang=language, slow=False)
    speech.save(file_name)
    playsound(file_name)
