class TradeDeduplicator:

    def deduplicate(self, trades):

        unique = {}

        duplicates = []

        for trade in trades:

            key = (

                trade["symbol"],
                trade["strategy"],
                trade.get("direction", "LONG")

            )

            if key in unique:

                duplicates.append(trade)

            else:

                unique[key] = trade

        return {

            "unique": list(unique.values()),

            "duplicates": duplicates

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("TRADE DEDUPLICATION")

        print("=" * 60)

        print()

        print("Unique Trades")

        for trade in report["unique"]:

            print(

                f"{trade['symbol']:<12}"

                f"{trade['strategy']:<12}"

                f"{trade.get('direction','LONG')}"

            )

        print()

        print("Duplicates")

        for trade in report["duplicates"]:

            print(

                f"{trade['symbol']:<12}"

                f"{trade['strategy']:<12}"

                f"{trade.get('direction','LONG')}"

            )