from datetime import datetime, UTC


class CandleBuilder:

    def __init__(self):

        self.current = None

    def update(self, price, volume=0):

        now = datetime.now(UTC)

        if self.current is None:

            self.current = {

                "open": price,

                "high": price,

                "low": price,

                "close": price,

                "volume": volume,

                "timestamp": now

            }

            return self.current

        self.current["high"] = max(

            self.current["high"],

            price

        )

        self.current["low"] = min(

            self.current["low"],

            price

        )

        self.current["close"] = price

        self.current["volume"] += volume

        return self.current

    def get_candle(self):

        return self.current

    def reset(self):

        self.current = None

    def print(self):

        if self.current is None:

            print("No candle")

            return

        print()

        print("=" * 60)

        print("CURRENT CANDLE")

        print("=" * 60)

        print()

        print("Open   :", self.current["open"])

        print("High   :", self.current["high"])

        print("Low    :", self.current["low"])

        print("Close  :", self.current["close"])

        print("Volume :", self.current["volume"])