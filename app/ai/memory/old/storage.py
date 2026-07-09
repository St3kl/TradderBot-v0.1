import json
from pathlib import Path

MEMORY_DIR = Path("data/memory")
MEMORY_DIR.mkdir(parents=True, exist_ok=True)


def load_json(filename):

    path = MEMORY_DIR / filename

    if not path.exists():
        return {}

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(filename, data):

    path = MEMORY_DIR / filename

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)