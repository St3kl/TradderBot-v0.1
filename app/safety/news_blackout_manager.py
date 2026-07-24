from datetime import datetime, timedelta, UTC


class NewsBlackoutManager:

    def __init__(self):

        self.events = []

    def add_event(self, name, event_time, blackout_before=30, blackout_after=30):

        self.events.append({

            "name": name,

            "time": event_time,

            "before": blackout_before,

            "after": blackout_after

        })

    def is_blackout(self):

        now = datetime.now(UTC)

        for event in self.events:

            start = event["time"] - timedelta(minutes=event["before"])
            end = event["time"] + timedelta(minutes=event["after"])

            if start <= now <= end:

                return True, event["name"]

        return False, None

    def print(self):

        active, event = self.is_blackout()

        print()
        print("=" * 60)
        print("NEWS BLACKOUT")
        print("=" * 60)
        print()

        print("Blackout :", active)

        if event:

            print("Event     :", event)