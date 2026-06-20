from core.voice import listen
from core.tts import speak
from core.storage import log_entry
from core.github import push, status
from brain.intent import detect_intent
from ui.jarvis_ui import UI
import threading
import os

ui = UI()

session_active = False


def voice_loop():
    global session_active

    while True:
        text = listen()
        if not text:
            continue

        lower = text.lower()
        ui.update(text)

        # WAKE
        if not session_active:
            if "leo" in lower:
                session_active = True
                speak("activated")
            continue

        # PAUSE
        if "pause" in lower:
            session_active = False
            speak("paused")
            continue

        print("YOU:", text)

        intent = detect_intent(text)

        # CATEGORY SYSTEM
        if intent == "category_add":
            speak("say category name")
            name = listen()

            if not name:
                continue

            name = name.lower().strip()
            os.makedirs(f"categories/{name}", exist_ok=True)

            speak("start speaking items, say that's all to stop")

            items = []

            while True:
                item = listen()
                if not item:
                    continue

                ui.update(item)

                if "that's all" in item.lower():
                    break

                items.append(item)

            with open(f"categories/{name}.txt", "a") as f:
                f.write("\n".join(items))

            speak("category saved")

        # GITHUB PUSH
        elif intent == "git_push":
            speak("commit message?")
            msg = listen() or "leo update"
            push(msg)
            speak("pushed")

        # GITHUB STATUS
        elif intent == "git_status":
            status()

        # README UPDATE
        elif intent == "readme":
            speak("say readme content")

            lines = []

            while True:
                line = listen()
                if not line:
                    continue

                ui.update(line)

                if "that's all" in line.lower():
                    break

                lines.append(line)

            with open("README.md", "a") as f:
                f.write("\n" + "\n".join(lines) + "\n")

            speak("readme updated")

        # HELP
        elif intent == "help":
            print("\n===== LEO OS COMMANDS =====")
            print("leo → activate")
            print("pause → stop system")
            print("create category → category mode")
            print("push this → git push")
            print("check status → git status")
            print("update readme → edit readme")
            print("===========================\n")

        # LOG
        else:
            log_entry({"text": text})


threading.Thread(target=voice_loop, daemon=True).start()

ui.run()