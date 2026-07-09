class PerformanceAnalyzer:
    """
    Computes performance statistics from completed trades.
    """

    def analyze(self, trades):

        if not trades:

            return {}

        total = len(trades)

        wins = [
            t for t in trades
            if t.get("result") == "WIN"
        ]

        losses = [
            t for t in trades
            if t.get("result") == "LOSS"
        ]

        gross_profit = sum(

            t.get("pnl", 0)

            for t in wins

        )

        gross_loss = abs(sum(

            t.get("pnl", 0)

            for t in losses

        ))

        win_rate = round(

            len(wins) / total * 100,

            2

        )

        avg_win = round(

            gross_profit / len(wins),

            2

        ) if wins else 0

        avg_loss = round(

            gross_loss / len(losses),

            2

        ) if losses else 0

        profit_factor = round(

            gross_profit / gross_loss,

            2

        ) if gross_loss else 0

        expectancy = round(

            (win_rate / 100 * avg_win)

            -

            ((100 - win_rate) / 100 * avg_loss),

            2

        )

        return {

            "total_trades": total,

            "wins": len(wins),

            "losses": len(losses),

            "win_rate": win_rate,

            "gross_profit": gross_profit,

            "gross_loss": gross_loss,

            "profit_factor": profit_factor,

            "average_win": avg_win,

            "average_loss": avg_loss,

            "expectancy": expectancy

        }