from datetime import datetime


class BrokerHeartbeat:

    def __init__(self, broker):

        self.broker = broker

        self.last_check = None

    def check(self):

        self.last_check = datetime.utcnow()

        alive = self.broker.is_connected()

        return {

            "alive": alive,

            "timestamp": self.last_check

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("BROKER HEARTBEAT")

        print("=" * 60)

        print()

        print("Alive     :", report["alive"])

        print("Timestamp :", report["timestamp"])