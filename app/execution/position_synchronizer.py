class PositionSynchronizer:

    def __init__(self):

        self.local_positions = []

    def synchronize(self, broker_positions):

        self.local_positions = broker_positions.copy()

        return self.local_positions

    def get_positions(self):

        return self.local_positions

    def count(self):

        return len(self.local_positions)

    def print(self):

        print()

        print("=" * 60)
        print("POSITION SYNCHRONIZATION")
        print("=" * 60)
        print()

        print("Open Positions:", self.count())

        if not self.local_positions:

            print("None")
            return

        for p in self.local_positions:

            print(

                p["symbol"],

                p["direction"],

                p["quantity"]

            )