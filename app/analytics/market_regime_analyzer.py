class MarketRegimeAnalyzer:

    def analyze(self, trades):

        regimes = {}

        for trade in trades:

            regime = trade.get("market_regime", "UNKNOWN")

            if regime not in regimes:

                regimes[regime] = {

                    "wins": 0,

                    "losses": 0,

                    "total": 0,

                    "win_rate": 0

                }

            regimes[regime]["total"] += 1

            if trade["result"] == "WIN":

                regimes[regime]["wins"] += 1

            else:

                regimes[regime]["losses"] += 1

        for regime in regimes.values():

            if regime["total"]:

                regime["win_rate"] = round(

                    regime["wins"] / regime["total"] * 100,

                    2

                )

        return regimes

    def print(self, regimes):

        print()

        print("=" * 60)

        print("MARKET REGIME ANALYSIS")

        print("=" * 60)

        for name, stats in regimes.items():

            print(

                f"{name:<15}"

                f" Trades:{stats['total']:<4}"

                f" WinRate:{stats['win_rate']}%"

            )