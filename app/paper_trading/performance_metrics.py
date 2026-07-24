class PerformanceMetrics:

    def calculate(self, trades):

        total = len(trades)

        winners = [t for t in trades if t["profit"] > 0]
        losers = [t for t in trades if t["profit"] <= 0]

        total_profit = sum(t["profit"] for t in trades)

        average_profit = (
            total_profit / total
            if total > 0
            else 0
        )

        win_rate = (
            (len(winners) / total) * 100
            if total > 0
            else 0
        )

        return {

            "total_trades": total,

            "winners": len(winners),

            "losers": len(losers),

            "win_rate": round(win_rate, 2),

            "total_profit": round(total_profit, 2),

            "average_profit": round(average_profit, 2)

        }

    def print(self, report):

        print()

        print("=" * 60)
        print("PERFORMANCE METRICS")
        print("=" * 60)
        print()

        print("Trades         :", report["total_trades"])
        print("Winners        :", report["winners"])
        print("Losers         :", report["losers"])
        print("Win Rate       :", report["win_rate"], "%")
        print("Total Profit   :", report["total_profit"])
        print("Average Profit :", report["average_profit"])