
import sounddevice as sd
from scipy.io.wavfile import write

def record_speech(duration):
    sampling_frequency = 48000
    
    recording_duration = duration

    audio_path = "recording0.wav"
    
    # Start recorder with the given values 
    # of duration and sample frequency
    recording = sd.rec(int(recording_duration * sampling_frequency), 
                    samplerate=sampling_frequency, channels=1)

    print("Sound recording started")

    sd.wait()
    
    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    write(audio_path, sampling_frequency, recording)

    print("Sound written to file")

    return audio_path