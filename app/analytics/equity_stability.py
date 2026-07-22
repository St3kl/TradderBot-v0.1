class EquityStability:

    def analyze(self, equity):

        if len(equity) < 2:

            return {

                "volatility": 0,

                "stability": 100

            }

        changes = []

        for i in range(1, len(equity)):

            changes.append(

                abs(

                    equity[i] - equity[i - 1]

                )

            )

        avg_change = sum(changes) / len(changes)

        stability = max(

            0,

            100 - avg_change / 10

        )

        return {

            "volatility": round(avg_change, 2),

            "stability": round(stability, 2)

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("EQUITY STABILITY")

        print("=" * 60)

        print()

        print("Average Change :", report["volatility"])

        print("Stability      :", report["stability"])