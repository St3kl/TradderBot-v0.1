class TradeAttribution:

    def analyze(self, trades):

        stats = {}

        for trade in trades:

            signals = trade.get("signals", [])

            result = trade.get("result", "")

            for signal in signals:

                if signal not in stats:

                    stats[signal] = {

                        "wins": 0,

                        "losses": 0,

                        "total": 0,

                    }

                stats[signal]["total"] += 1

                if result == "WIN":

                    stats[signal]["wins"] += 1

                elif result == "LOSS":

                    stats[signal]["losses"] += 1

        for signal in stats.values():

            total = signal["total"]

            signal["win_rate"] = (

                round(signal["wins"] / total * 100, 2)

                if total else 0

            )

        return dict(

            sorted(

                stats.items(),

                key=lambda x: x[1]["win_rate"],

                reverse=True,

            )

        )