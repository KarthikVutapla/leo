import json
import os
from datetime import datetime

def log_entry(data):
    os.makedirs("data", exist_ok=True)

    file = f"data/{datetime.now().date()}.json"

    try:
        with open(file, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(data)

    with open(file, "w") as f:
        json.dump(logs, f, indent=2)