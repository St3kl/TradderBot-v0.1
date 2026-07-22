class StrategyInsights:

    def analyze(self, strategy_stats):

        insights = []

        for strategy, stats in strategy_stats.items():

            winrate = stats.get("win_rate", 0)
            total = stats.get("total", 0)

            if total < 10:

                insights.append(
                    f"{strategy}: Not enough trades for reliable analysis."
                )

            elif winrate >= 70:

                insights.append(
                    f"{strategy}: Excellent performance ({winrate}%). Increase usage."
                )

            elif winrate >= 55:

                insights.append(
                    f"{strategy}: Stable performance ({winrate}%). Keep monitoring."
                )

            elif winrate >= 40:

                insights.append(
                    f"{strategy}: Weak edge ({winrate}%). Review entry conditions."
                )

            else:

                insights.append(
                    f"{strategy}: Poor performance ({winrate}%). Disable or redesign."
                )

        return insights

    def print(self, insights):

        print()

        print("=" * 60)
        print("STRATEGY INSIGHTS")
        print("=" * 60)

        for item in insights:

            print("-", item)