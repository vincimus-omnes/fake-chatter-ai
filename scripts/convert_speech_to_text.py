import whisper

def convert_speech(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]

# convert_speech("recording0.wav")