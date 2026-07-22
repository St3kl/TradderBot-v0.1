class RecoveryFactor:

    def analyze(self, trades):

        total_profit = sum(

            t["profit"]

            for t in trades

        )

        max_drawdown = max(

            (t.get("drawdown", 0)

             for t in trades),

            default=0

        )

        if max_drawdown == 0:

            factor = 0

        else:

            factor = total_profit / max_drawdown

        return {

            "profit": round(total_profit, 2),

            "drawdown": round(max_drawdown, 2),

            "recovery_factor": round(factor, 2)

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("RECOVERY FACTOR")

        print("=" * 60)

        print()

        print("Net Profit      :", report["profit"])

        print("Max Drawdown    :", report["drawdown"])

        print("Recovery Factor :", report["recovery_factor"])