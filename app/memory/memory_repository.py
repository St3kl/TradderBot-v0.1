import json
import os


class MemoryRepository:

    def __init__(self):

        self.filename = "database/trade_memory.json"

        os.makedirs("database", exist_ok=True)

        if not os.path.exists(self.filename):

            with open(self.filename, "w") as f:

                json.dump([], f)

    def load(self):

        with open(self.filename, "r") as f:

            return json.load(f)

    def save(self, memory):

        data = self.load()

        data.append(memory)

        with open(self.filename, "w") as f:

            json.dump(data, f, indent=4)