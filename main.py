from ui.jarvis_ui import JarvisUI
from core.voice import listen_audio
from core.tts import speak
import threading

ui = JarvisUI()

active = False


def brain_loop():
    global active

    while True:
        text, volume = listen_audio()

        if volume:
            ui.update_wave(volume)

        if not text:
            continue

        lower = text.lower()

        # WAKE WORD (ANY leo mention)
        if not active:
            if "leo" in lower:
                active = True
                ui.set_text("LEO ACTIVATED")
                speak("Yes")
            continue

        # PAUSE
        if "pause" in lower:
            active = False
            ui.set_text("LEO PAUSED")
            speak("Paused")
            continue

        ui.set_text(text)

        # SIMPLE RESPONSES (expand later)
        if "hello" in lower:
            speak("Hello")

        elif "how are you" in lower:
            speak("I am fine")

        elif "your name" in lower:
            speak("I am Leo")

        else:
            speak("Done")


threading.Thread(target=brain_loop, daemon=True).start()

ui.run()