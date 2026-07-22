class PerformanceDashboard:

    def summarize(self, trades):

        if not trades:
            return {}

        total = len(trades)

        wins = sum(
            1 for t in trades
            if t["result"] == "WIN"
        )

        losses = total - wins

        pnl = sum(
            t.get("profit", 0)
            for t in trades
        )

        average = pnl / total

        winrate = wins / total * 100

        average_win = 0
        average_loss = 0

        win_trades = [
            t.get("profit", 0)
            for t in trades
            if t["result"] == "WIN"
        ]

        loss_trades = [
            t.get("profit", 0)
            for t in trades
            if t["result"] == "LOSS"
        ]

        if win_trades:
            average_win = sum(win_trades) / len(win_trades)

        if loss_trades:
            average_loss = sum(loss_trades) / len(loss_trades)

        expectancy = average

        profit_factor = 0

        gross_profit = sum(
            p for p in win_trades
        )

        gross_loss = abs(sum(loss_trades))

        if gross_loss > 0:
            profit_factor = gross_profit / gross_loss

        return {

            "total_trades": total,

            "wins": wins,

            "losses": losses,

            "win_rate": round(winrate, 2),

            "net_profit": round(pnl, 2),

            "average_trade": round(average, 2),

            "average_win": round(average_win, 2),

            "average_loss": round(average_loss, 2),

            "profit_factor": round(profit_factor, 2),

            "expectancy": round(expectancy, 2),

        }