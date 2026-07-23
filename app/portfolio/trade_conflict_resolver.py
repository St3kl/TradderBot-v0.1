class TradeConflictResolver:

    def resolve(self, trades):

        resolved = {}
        rejected = []

        for trade in trades:

            symbol = trade["symbol"]

            if symbol not in resolved:

                resolved[symbol] = trade

                continue

            current = resolved[symbol]

            if trade["priority"] > current["priority"]:

                rejected.append(current)

                resolved[symbol] = trade

            else:

                rejected.append(trade)

        return {

            "approved": list(resolved.values()),

            "rejected": rejected

        }

    def print(self, report):

        print()

        print("=" * 60)
        print("TRADE CONFLICT RESOLUTION")
        print("=" * 60)
        print()

        print("Approved")

        for trade in report["approved"]:

            print(

                f"{trade['symbol']:<12}"

                f"{trade['strategy']:<12}"

                f"{trade['priority']}"

            )

        print()

        print("Rejected")

        for trade in report["rejected"]:

            print(

                f"{trade['symbol']:<12}"

                f"{trade['strategy']:<12}"

                f"{trade['priority']}"

            )