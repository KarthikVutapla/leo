import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak now...")
        r.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        except:
            print("Mic timeout")
            return None

    try:
        text = r.recognize_google(audio)
        return text

    except sr.UnknownValueError:
        print("Could not understand audio")
        return None

    except sr.RequestError:
        print("Network error (Google API failed)")
        return None