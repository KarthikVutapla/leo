import speech_recognition as sr
import numpy as np
import audioop

r = sr.Recognizer()

def listen_audio():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.3)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
    except:
        text = None

    # convert raw audio for waveform intensity
    try:
        volume = audioop.rms(audio.frame_data, 2)
    except:
        volume = 0

    return text, volume