from speech import listen
from core.intent import detect_intent
from core.storage import log_entry
from core.github import push, status
import os

current_category = None


# ---------------- CATEGORY FLOW ----------------

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
    print("Now speak items. Say 'that's all' to finish")

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


# ---------------- LOG MODE ----------------

def log_mode(text):
    log_entry({
        "type": "log",
        "text": text
    })

    print("Logged:", text)


# ---------------- MAIN ----------------

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
        print("Pushing to GitHub...")
        push()

    elif intent == "git_status":
        print("Repo status:")
        status()

    elif intent == "exit":
        print("Shutting down Leo...")
        break

    else:
        log_mode(text)