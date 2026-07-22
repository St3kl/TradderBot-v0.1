class ExpectancyAnalyzer:

    def analyze(self, trades):

        if not trades:

            return 0

        profits = [

            t["profit"]

            for t in trades

        ]

        return round(

            sum(profits) / len(profits),

            2

        )