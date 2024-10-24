from scripts.get_speech import record_speech
from scripts.convert_speech_to_text import convert_speech
from scripts.tts import convert_text_and_play
from scripts.llm import prompt_llm
from scripts.chat_messages import get_new_lines

last_line_read = -1
twitch_log = 'twitch_chat_log.txt'

def main_loop():
    duration = 20

    audio_path = record_speech(duration)

    converted_speech_text = convert_speech(audio_path)

    global last_line_read

    lines, last_line_read = get_new_lines(twitch_log, last_line_read)

    prompt = "Your response must be 150 characters or less.\n"
    prompt += "Do not mention metrics of any kind such as: Followers, Subscribers, Number of Viewers \n"
    prompt += "Take the following list of chat messages and either choose an interesting "
    prompt += "one to repeat in your own words in 150 characters or less:\n"
    prompt += "[Chat messages]\n"
    for line in lines:
        prompt += line + "\n"
    prompt += "[End of chat messages]\n"
    prompt += "if none of the chat messages are interesting or there are no chat messages then "
    prompt += """while ignoring any pauses or breaks in train of thought in 150 characters or less
    ask an interesting question or make an interesting observation about 
    the following transcript from my livestream: \n"""
    prompt += "[Transcript]"
    prompt += converted_speech_text
    prompt += "[End of transcript]"
    prompt += "If there is no transcript and no chat messages then your response should be completely empty."

    print("Beginning LLM prompt")
    llm_response = prompt_llm(prompt)

    convert_text_and_play(llm_response)

    print(prompt)
    print(converted_speech_text)
    print(llm_response)



if __name__ == "__main__":

    while(True):
        main_loop()
        # Split into separate prompts
