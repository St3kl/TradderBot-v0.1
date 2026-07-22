class ResearchScore:
    """
    Computes a weighted research score
    for every optimization result.
    """

    def score(

        self,

        metrics

    ):

        win_rate = metrics["win_rate"]

        profit_factor = metrics["profit_factor"]

        sharpe = metrics["sharpe"]

        drawdown = metrics["drawdown"]

        score = (

            win_rate * 0.40 +

            profit_factor * 20 +

            sharpe * 10 -

            drawdown * 0.20

        )

        return round(score, 2)