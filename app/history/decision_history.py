import json
from datetime import datetime
import os



class DecisionHistory:

    def __init__(self):

        self.filename = "logs/decision_history.json"

        os.makedirs("logs", exist_ok=True)

        if not os.path.exists(self.filename):

            with open(self.filename, "w") as f:

                json.dump([], f)
    def save(self, session):

        with open(self.filename, "r") as f:

            data = json.load(f)

        data.append({

            "symbol": session.symbol,

            "decision": session.decision,

            "confidence": session.decision["confidence"]

        })

        with open(self.filename, "w") as f:

            json.dump(data, f, indent=4)