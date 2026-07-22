class WinrateAnalyzer:

    def analyze(self, trades):

        if not trades:

            return {}

        wins = sum(1 for t in trades if t["result"] == "WIN")
        losses = sum(1 for t in trades if t["result"] == "LOSS")

        total = wins + losses

        return {

            "wins": wins,

            "losses": losses,

            "total": total,

            "win_rate": round(wins / total * 100, 2)

        }