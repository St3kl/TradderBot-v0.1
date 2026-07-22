class StrategyScore:

    def calculate(self, stats):

        total = stats.get("total", 0)

        if total < 20:
            return 50

        winrate = stats["win_rate"]

        score = (

            winrate * 0.70

            +

            min(total, 200) / 200 * 30

        )

        return round(score, 2)