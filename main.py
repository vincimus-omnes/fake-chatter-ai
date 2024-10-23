from scripts.get_speech import record_speech
from scripts.convert_speech_to_text import convert_speech
from scripts.tts import convert_text_and_play
from scripts.llm import prompt_llm

def main_loop():
    duration = 10

    audio_path = record_speech(duration)

    converted_speech_text = convert_speech(audio_path)

    prompt = "Your response must be 150 characters or less.\n"
    prompt += "Do not mention metrics of any kind such as: Followers, Subscribers, Number of Viewers \n"
    prompt += "Take the following list of chat messages and either choose an interesting "
    prompt += "one to repeat in your own words in 150 characters or less:\n"
    prompt += "[Chat messages]\n"
    # Chat messages go here
    prompt += "[End of chat messages]\n"
    prompt += "if none of the chat messages are interesting or there are no chat messages then "
    prompt += """while ignoring any pauses or breaks in train of thought in 150 characters or less
    ask an interesting question or make an interesting observation about 
    the following transcript from my livestream: \n"""
    prompt += "[Transcript]"
    prompt += converted_speech_text
    prompt += "[End of transcript]"
    prompt += "If there is no transcript and no chat messages then your response should be completely empty."

    llm_response = prompt_llm(prompt)

    convert_text_and_play(llm_response)

    print(converted_speech_text)
    print(llm_response)

def test_prompt():
    prompt = "Your response must be 150 characters or less.\n"
    prompt += "Your response should only contain one statement or question.\n"
    prompt += "Do not tell me you are ready to respond or waiting for further input \n"
    prompt += "Do not mention metrics of any kind such as: Followers, Subscribers, Number of Viewers \n"
    prompt += "Take the following list of chat messages and either choose an interesting "
    prompt += "one to repeat in your own words in 150 characters or less:\n"
    prompt += "[Chat messages]\n"
    # Chat messages go here
    prompt += "[End of chat messages]\n"
    prompt += "if none of the chat messages are interesting or there are no chat messages then "
    prompt += "while ignoring any pauses or breaks in train of thought in 150 characters or less \
    ask an interesting question or make an interesting observation about \
    the following transcript from my livestream: \n"
    prompt += "[Transcript]\n"
    prompt += "[End of transcript]\n"

    llm_response = prompt_llm(prompt)
    print(llm_response)

while(1):
    test_prompt()