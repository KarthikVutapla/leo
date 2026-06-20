from rapidfuzz import fuzz

def detect_intent(text):
    if not text:
        return "unknown"

    text = text.lower()

    patterns = {
        "category_add": [
            "create category",
            "make category",
            "add category",
            "new category"
        ],

        "git_push": [
            "push this",
            "sync repo",
            "commit this",
            "save to github"
        ],

        "git_status": [
            "check status",
            "git status",
            "what changed"
        ],

        "readme": [
            "update readme",
            "edit readme",
            "add to readme"
        ],

        "help": [
            "what can you do",
            "help me",
            "leo what can you do",
            "what are your commands"
        ],

        "exit": [
            "bye leo",
            "shutdown",
            "stop leo"
        ]
    }

    for intent, phrases in patterns.items():
        for p in phrases:
            if fuzz.partial_ratio(text, p) > 80:
                return intent

    return "log"