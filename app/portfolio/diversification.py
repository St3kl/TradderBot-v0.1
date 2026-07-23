class DiversificationEngine:

    def analyze(self, positions):

        assets = {}
        strategies = {}

        for position in positions:

            asset = position["symbol"]
            strategy = position["strategy"]

            assets[asset] = assets.get(asset, 0) + 1
            strategies[strategy] = strategies.get(strategy, 0) + 1

        total = len(positions)

        asset_distribution = {}

        strategy_distribution = {}

        for asset, count in assets.items():

            asset_distribution[asset] = round(

                count / total * 100,

                2

            )

        for strategy, count in strategies.items():

            strategy_distribution[strategy] = round(

                count / total * 100,

                2

            )

        return {

            "assets": asset_distribution,

            "strategies": strategy_distribution,

            "positions": total

        }

    def print(self, report):

        print()

        print("=" * 60)
        print("PORTFOLIO DIVERSIFICATION")
        print("=" * 60)

        print()

        print("Assets")

        for asset, percent in report["assets"].items():

            print(f"{asset:<10} {percent}%")

        print()

        print("Strategies")

        for strategy, percent in report["strategies"].items():

            print(f"{strategy:<10} {percent}%")