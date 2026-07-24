from datetime import datetime, UTC


class AutoRecoveryManager:

    def __init__(self):

        self.history = []

    def recover(self, service_name):

        event = {
            "service": service_name,
            "status": "RECOVERED",
            "time": datetime.now(UTC)
        }

        self.history.append(event)

        return True

    def get_history(self):

        return self.history

    def print(self):

        print()
        print("=" * 60)
        print("AUTO RECOVERY")
        print("=" * 60)
        print()

        if not self.history:
            print("No recovery events")
            return

        for event in self.history:

            print(
                event["time"],
                event["service"],
                event["status"]
            )