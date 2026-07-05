from app.analytics.equity_curve import EquityCurveEngine


class DrawdownEngine:

    def __init__(self):

        self.curve = EquityCurveEngine()

    def maximum_drawdown(self):

        equity = self.curve.build_curve()

        peak = equity[0]

        max_dd = 0.0

        for value in equity:

            if value > peak:

                peak = value

            drawdown = ((peak - value) / peak) * 100

            if drawdown > max_dd:

                max_dd = drawdown

        return round(max_dd, 2)
    