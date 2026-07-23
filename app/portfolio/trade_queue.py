class TradeQueue:

    def __init__(self):

        self.queue = []

    def add(self, trade):

        self.queue.append(trade)

        self.queue.sort(

            key=lambda t: t["confidence"],

            reverse=True

        )

    def pop(self):

        if not self.queue:

            return None

        return self.queue.pop(0)

    def pending(self):

        return len(self.queue)

    def clear(self):

        self.queue.clear()

    def print(self):

        print()

        print("=" * 60)

        print("TRADE QUEUE")

        print("=" * 60)

        print()

        for trade in self.queue:

            print(

                f"{trade['symbol']:<12}"

                f"{trade['strategy']:<12}"

                f"{trade['confidence']}"

            )