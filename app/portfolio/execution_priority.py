class ExecutionPriority:

    def calculate(self, trade):

        confidence = trade.get("confidence", 0)
        quality = trade.get("quality", 0)
        expectancy = trade.get("expectancy", 0)
        market = trade.get("market_health", 50)

        priority = (

            confidence * 0.40 +

            quality * 0.25 +

            expectancy * 0.20 +

            market * 0.15

        )

        return round(priority, 2)

    def rank(self, trades):

        for trade in trades:

            trade["priority"] = self.calculate(trade)

        trades.sort(

            key=lambda t: t["priority"],

            reverse=True

        )

        return trades

    def print(self, trades):

        print()

        print("=" * 60)

        print("EXECUTION PRIORITY")

        print("=" * 60)

        print()

        for trade in trades:

            print(

                f"{trade['symbol']:<12}"

                f"{trade['priority']:>7}"

            )