class ExecutionScheduler:

    def __init__(self, max_positions=3):

        self.max_positions = max_positions

    def schedule(self, queue, open_positions):

        available = self.max_positions - open_positions

        if available <= 0:

            return []

        return queue[:available]

    def print(self, trades):

        print()

        print("=" * 60)
        print("EXECUTION SCHEDULE")
        print("=" * 60)
        print()

        if not trades:

            print("No trades scheduled.")
            return

        for trade in trades:

            print(

                f"{trade['symbol']:<12}"

                f"{trade['priority']:>7}"

            )