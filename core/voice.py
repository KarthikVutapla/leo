import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.4)
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except:
        return None