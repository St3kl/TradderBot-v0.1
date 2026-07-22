class BestTradeProfile:

    def analyze(self, trades):

        profile = {

            "signals": {},

            "strategies": {},

            "market_regimes": {}

        }

        winners = [

            t for t in trades

            if t.get("result") == "WIN"

        ]

        for trade in winners:

            # Signals

            for signal in trade.get("signals", []):

                profile["signals"][signal] = (

                    profile["signals"].get(signal, 0) + 1

                )

            # Strategy

            strategy = trade.get("strategy", "UNKNOWN")

            profile["strategies"][strategy] = (

                profile["strategies"].get(strategy, 0) + 1

            )

            # Market Regime

            regime = trade.get(

                "market_regime",

                "UNKNOWN"

            )

            profile["market_regimes"][regime] = (

                profile["market_regimes"].get(regime, 0) + 1

            )

        return profile

    def print(self, profile):

        print()

        print("=" * 60)

        print("BEST TRADE PROFILE")

        print("=" * 60)

        print()

        print("Signals")

        for k, v in sorted(

            profile["signals"].items(),

            key=lambda x: x[1],

            reverse=True

        ):

            print(f"{k:<25}{v}")

        print()

        print("Strategies")

        for k, v in sorted(

            profile["strategies"].items(),

            key=lambda x: x[1],

            reverse=True

        ):

            print(f"{k:<25}{v}")

        print()

        print("Market Regimes")

        for k, v in sorted(

            profile["market_regimes"].items(),

            key=lambda x: x[1],

            reverse=True

        ):

            print(f"{k:<25}{v}")