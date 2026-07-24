from datetime import datetime, UTC


class TickAggregator:

    def __init__(self):

        self.ticks = []

    def add_tick(self, price, volume=0):

        self.ticks.append({

            "price": price,

            "volume": volume,

            "timestamp": datetime.now(UTC)

        })

    def count(self):

        return len(self.ticks)

    def latest(self):

        if not self.ticks:
            return None

        return self.ticks[-1]

    def all(self):

        return self.ticks

    def clear(self):

        self.ticks.clear()

    def print(self):

        print()

        print("=" * 60)

        print("TICK AGGREGATOR")

        print("=" * 60)

        print()

        print("Ticks :", self.count())

        if self.latest():

            print("Latest:", self.latest())