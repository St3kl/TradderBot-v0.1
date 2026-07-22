class TradeBlueprint:

    def build(self, profile, combinations):

        blueprint = {

            "ideal_signals": [],

            "ideal_strategy": None,

            "ideal_market": None,

            "best_combinations": []

        }

        # Top Signals

        blueprint["ideal_signals"] = sorted(

            profile["signals"],

            key=profile["signals"].get,

            reverse=True

        )[:5]

        # Best Strategy

        if profile["strategies"]:

            blueprint["ideal_strategy"] = max(

                profile["strategies"],

                key=profile["strategies"].get

            )

        # Best Market

        if profile["market_regimes"]:

            blueprint["ideal_market"] = max(

                profile["market_regimes"],

                key=profile["market_regimes"].get

            )

        # Best Signal Combinations

        ranking = sorted(

            combinations.items(),

            key=lambda x: x[1]["win_rate"],

            reverse=True

        )

        blueprint["best_combinations"] = [

            combo for combo, _ in ranking[:5]

        ]

        return blueprint

    def print(self, blueprint):

        print()

        print("=" * 60)

        print("IDEAL TRADE BLUEPRINT")

        print("=" * 60)

        print()

        print("Best Strategy")

        print(blueprint["ideal_strategy"])

        print()

        print("Best Market")

        print(blueprint["ideal_market"])

        print()

        print("Preferred Signals")

        for signal in blueprint["ideal_signals"]:

            print("-", signal)

        print()

        print("Preferred Signal Combinations")

        for combo in blueprint["best_combinations"]:

            print("-", combo)