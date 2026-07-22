class StrategyAdvisor:

    def review(self, strategy_stats):

        advice = []

        for name, stats in strategy_stats.items():

            if stats["total"] < 20:

                continue

            if stats["win_rate"] < 45:

                advice.append(

                    f"{name}: Disable temporarily."

                )

            elif stats["win_rate"] > 65:

                advice.append(

                    f"{name}: Increase priority."

                )

        return advice