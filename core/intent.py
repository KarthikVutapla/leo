from rapidfuzz import fuzz

def detect_intent(text):
    if not text:
        return "unknown"

    text = text.lower()

    patterns = {
        "create_category": [
            "create category",
            "make category",
            "add category",
            "new category",
            "i want a category",
            "help me create a category"
        ],

        "git_push": [
            "push this",
            "push to github",
            "commit this",
            "sync repo",
            "save to github"
        ],

        "git_status": [
            "check status",
            "git status",
            "what changed",
            "repo status"
        ],

        "help": [
            "what can you do",
            "what can you do leo",
            "help me",
            "rio what can you do"
        ],

        "exit": [
            "bye leo",
            "shutdown",
            "stop leo",
            "exit"
        ]
    }

    for intent, phrases in patterns.items():
        for p in phrases:
            if fuzz.partial_ratio(text, p) > 80:
                return intent

    return "log"