from datetime import datetime


class OrderEventLogger:

    def __init__(self):

        self.events = []

    def log(

        self,

        order_id,

        event,

        details=None

    ):

        self.events.append({

            "timestamp": datetime.utcnow(),

            "order_id": order_id,

            "event": event,

            "details": details or {}

        })

    def get_events(self, order_id=None):

        if order_id is None:

            return self.events

        return [

            e

            for e in self.events

            if e["order_id"] == order_id

        ]

    def print(self, order_id=None):

        print()

        print("=" * 60)

        print("ORDER EVENTS")

        print("=" * 60)

        print()

        for event in self.get_events(order_id):

            print(

                event["timestamp"],

                event["order_id"],

                event["event"],

                event["details"]

            )