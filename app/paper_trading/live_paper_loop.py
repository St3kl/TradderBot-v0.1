import time
from datetime import datetime, UTC

datetime.now(UTC)


class LivePaperTradingLoop:

    def __init__(

        self,

        analyzer,

        interval=5

    ):

        self.analyzer = analyzer
        self.interval = interval
        self.running = False

    def start(

        self,

        iterations=None

    ):

        self.running = True

        count = 0

        while self.running:

            print()

            print("=" * 60)
            print("LIVE PAPER TRADING LOOP")
            print("=" * 60)

            print()

            print(

                "Time:",

                datetime.now()

            )

            result = self.analyzer()

            print(

                "Analyzer:",

                result

            )

            count += 1

            if iterations is not None and count >= iterations:
                break

            time.sleep(self.interval)

        self.running = False

    def stop(self):

        self.running = False