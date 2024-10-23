from get_speech import record_speech
from convert_speech_to_text import convert_speech
from tts import convert_text_and_play
from llm import prompt_llm

duration = 5

audio_path = record_speech(duration)

converted_speech_text = convert_speech(audio_path)

llm_response = prompt_llm()

convert_text_and_play(llm_response)