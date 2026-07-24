from datetime import datetime


class TradeJournal:

    def __init__(self):

        self.trades = []

    def record(self, trade):

        record = trade.copy()

        record["recorded_at"] = datetime.utcnow()

        self.trades.append(record)

    def all(self):

        return self.trades

    def winners(self):

        return [

            t

            for t in self.trades

            if t["profit"] > 0

        ]

    def losers(self):

        return [

            t

            for t in self.trades

            if t["profit"] <= 0

        ]

    def summary(self):

        return {

            "total": len(self.trades),

            "winners": len(self.winners()),

            "losers": len(self.losers())

        }

    def print(self):

        s = self.summary()

        print()

        print("=" * 60)

        print("TRADE JOURNAL")

        print("=" * 60)

        print()

        print("Total Trades :", s["total"])

        print("Winners      :", s["winners"])

        print("Losers       :", s["losers"])

        print()

        for trade in self.trades:

            print(

                trade["symbol"],

                trade["strategy"],

                trade["profit"]

            )