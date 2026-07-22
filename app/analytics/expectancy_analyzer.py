class ExpectancyAnalyzer:

    def analyze(self, trades):

        if not trades:

            return {

                "expectancy": 0,

                "average_win": 0,

                "average_loss": 0,

                "win_rate": 0

            }

        wins = [

            t["profit"]

            for t in trades

            if t["profit"] > 0

        ]

        losses = [

            abs(t["profit"])

            for t in trades

            if t["profit"] < 0

        ]

        avg_win = (

            sum(wins) / len(wins)

            if wins else 0

        )

        avg_loss = (

            sum(losses) / len(losses)

            if losses else 0

        )

        win_rate = (

            len(wins) / len(trades)

        )

        loss_rate = 1 - win_rate

        expectancy = (

            (win_rate * avg_win)

            -

            (loss_rate * avg_loss)

        )

        return {

            "expectancy": round(expectancy, 2),

            "average_win": round(avg_win, 2),

            "average_loss": round(avg_loss, 2),

            "win_rate": round(win_rate * 100, 2)

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("EXPECTANCY ANALYSIS")

        print("=" * 60)

        print()

        print("Win Rate      :", report["win_rate"], "%")

        print("Average Win   :", report["average_win"])

        print("Average Loss  :", report["average_loss"])

        print("Expectancy    :", report["expectancy"])