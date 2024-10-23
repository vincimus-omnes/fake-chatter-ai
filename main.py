from scripts.get_speech import record_speech
from scripts.convert_speech_to_text import convert_speech
from scripts.tts import convert_text_and_play
from scripts.llm import prompt_llm

duration = 5

audio_path = record_speech(duration)

converted_speech_text = convert_speech(audio_path)

llm_response = prompt_llm(converted_speech_text)

convert_text_and_play(llm_response)

print(converted_speech_text)
print(llm_response)