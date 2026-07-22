from itertools import combinations


class SignalCombinationAnalyzer:

    def analyze(self, trades):

        combos = {}

        for trade in trades:

            signals = sorted(trade.get("signals", []))

            if len(signals) < 2:
                continue

            for combo in combinations(signals, 2):

                key = " + ".join(combo)

                if key not in combos:

                    combos[key] = {

                        "wins": 0,

                        "losses": 0,

                        "total": 0,

                        "win_rate": 0

                    }

                combos[key]["total"] += 1

                if trade["result"] == "WIN":

                    combos[key]["wins"] += 1

                else:

                    combos[key]["losses"] += 1

        for stats in combos.values():

            if stats["total"]:

                stats["win_rate"] = round(

                    stats["wins"] /

                    stats["total"] * 100,

                    2

                )

        return combos

    def print(self, combos):

        print()

        print("=" * 60)

        print("SIGNAL COMBINATIONS")

        print("=" * 60)

        ranking = sorted(

            combos.items(),

            key=lambda x: x[1]["win_rate"],

            reverse=True

        )

        for combo, stats in ranking:

            print(

                f"{combo:<40}"

                f"{stats['win_rate']}%"

                f" ({stats['wins']}/{stats['total']})"

            )