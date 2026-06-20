from speech import listen
from core.intent import detect_intent
from core.storage import log_entry
from core.github import status
import os

current_category = None


def show_help():
    print("\n========= LEO COMMANDS =========\n")

    print("🟢 CATEGORY")
    print("- create category / make category")
    print("  → creates a new folder and stores items\n")

    print("🟡 LOGGING")
    print("- normal speech (no command)")
    print("  → stores in daily memory file\n")

    print("🔵 GITHUB")
    print("- push this / sync repo")
    print("  → asks for commit message, then pushes to GitHub\n")

    print("- check status")
    print("  → shows git status\n")

    print("🔴 EXIT")
    print("- bye leo / shutdown")
    print("  → exits program\n")

    print("==============================\n")


def create_category_flow():
    global current_category

    print("Say category name")

    name = listen()
    if not name:
        return

    name = name.lower().strip()
    current_category = name

    os.makedirs(f"categories/{name}", exist_ok=True)

    print(f"Category created: {name}")
    print("Speak items. Say 'that's all' to finish")

    while True:
        text = listen()

        if not text:
            continue

        print(">>", text)

        if "that" in text.lower():
            break

        log_entry({
            "type": "category_item",
            "category": current_category,
            "text": text
        })


def log_mode(text):
    log_entry({
        "type": "log",
        "text": text
    })

    print("Logged:", text)


print("LEO ACTIVE")

while True:
    text = listen()

    if not text:
        continue

    print("YOU:", text)

    intent = detect_intent(text)

    if intent == "create_category":
        create_category_flow()

    elif intent == "git_push":
        print("What should be the commit message?")

        msg = listen()

        if not msg:
            msg = "Leo update"

        print("Committing with message:", msg)

        os.system("git add .")
        os.system(f'git commit -m "{msg}"')
        os.system("git push")

    elif intent == "git_status":
        print("Repo status:")
        status()

    elif intent == "help":
        show_help()

    elif intent == "exit":
        print("Shutting down Leo...")
        break

    else:
        log_mode(text)