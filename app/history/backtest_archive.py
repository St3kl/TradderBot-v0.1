import json
import os
from datetime import datetime


class BacktestArchive:

    def __init__(self, filename="logs/backtest_archive.json"):

        self.filename = filename

        os.makedirs(os.path.dirname(filename), exist_ok=True)

    def save(self, report):

        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "report": report
        }

        history = []

        if os.path.exists(self.filename):

            try:
                with open(self.filename, "r") as f:
                    history = json.load(f)
            except:
                history = []

        history.append(entry)

        with open(self.filename, "w") as f:
            json.dump(history, f, indent=4)

    def load(self):

        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as f:
            return json.load(f)

    def latest(self):

        history = self.load()

        if not history:
            return None

        return history[-1]