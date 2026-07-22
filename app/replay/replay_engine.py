import json
import os


class ReplayEngine:

    def __init__(self):

        self.filename = "logs/replay.json"

        os.makedirs("logs", exist_ok=True)

    def save(self, session):

        replay = {

            "symbol": session.symbol,

            "trend": session.trend,

            "structure": session.structure,

            "smart_money": session.smart_money,

            "confluence": session.confluence,

            "decision": session.decision,

            "trade": session.trade,

            "result": getattr(session, "result", None),

        }

        with open(self.filename, "a") as f:

            f.write(json.dumps(replay, default=str))

            f.write("\n")