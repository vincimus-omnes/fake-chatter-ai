from gtts import gTTS
from playsound import playsound
import multiprocessing

file_name = "recording1.mp3"


def convert_text_and_play(text_to_convert):
    language = 'en'
    speech = gTTS(text=text_to_convert, lang=language, slow=False)
    speech.save(file_name)
    playsound(file_name)

def play_sound_and_exit():
    p = multiprocessing.Process(target=playsound, args=(file_name,))
    p.start()
    p.join() 
    p.terminate()