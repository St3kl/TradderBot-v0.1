class MarketAdvisor:

    def review(self, market_stats):

        advice = []

        for regime, stats in market_stats.items():

            if stats["total"] < 20:

                continue

            if stats["win_rate"] < 40:

                advice.append(

                    f"Avoid trading during {regime}"

                )

        return advice