from app.statistics.equity_curve import EquityCurve


class DrawdownEngine:

    def __init__(self):

        self.curve = EquityCurve()

    def build(self):

        equity = self.curve.build()

        if not equity:

            return {}

        peak = equity[0]["balance"]

        max_drawdown = 0

        current_drawdown = 0

        for point in equity:

            balance = point["balance"]

            if balance > peak:

                peak = balance

            drawdown = peak - balance

            if drawdown > max_drawdown:

                max_drawdown = drawdown

            current_drawdown = drawdown

        drawdown_percent = 0

        if peak > 0:

            drawdown_percent = (

                max_drawdown / peak

            ) * 100

        return {

            "peak_equity": round(peak, 2),

            "maximum_drawdown": round(max_drawdown, 2),

            "maximum_drawdown_percent": round(drawdown_percent, 2),

            "current_drawdown": round(current_drawdown, 2)

        }