class EdgeAnalyzer:

    def analyze(self, trades):

        edges = {}

        for trade in trades:

            for signal in trade.get("signals", []):

                if signal not in edges:

                    edges[signal] = {

                        "wins": 0,

                        "losses": 0,

                        "total": 0,

                        "win_rate": 0

                    }

                edges[signal]["total"] += 1

                if trade["result"] == "WIN":

                    edges[signal]["wins"] += 1

                else:

                    edges[signal]["losses"] += 1

        for signal in edges.values():

            if signal["total"]:

                signal["win_rate"] = round(

                    signal["wins"] /

                    signal["total"] * 100,

                    2

                )

        return edges

    def print(self, edges):

        print()

        print("=" * 60)

        print("EDGE ANALYSIS")

        print("=" * 60)

        ranking = sorted(

            edges.items(),

            key=lambda x: x[1]["win_rate"],

            reverse=True

        )

        for name, stats in ranking:

            print(

                f"{name:<25}"

                f"{stats['win_rate']}%"

                f" ({stats['wins']}/{stats['total']})"

            )