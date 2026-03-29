import json
import os

def save(subject, data):
    os.makedirs("data/saved", exist_ok=True)
    file = f"data/saved/{subject}.json"

    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def load(subject):
    file = f"data/saved/{subject}.json"

    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return None