from app.statistics.statistics_engine import StatisticsEngine
from app.statistics.metrics_engine import MetricsEngine
from app.statistics.equity_curve import EquityCurve
from app.statistics.drawdown_engine import DrawdownEngine


class DashboardEngine:

    def __init__(self):

        self.statistics = StatisticsEngine()

        self.metrics = MetricsEngine()

        self.equity = EquityCurve()

        self.drawdown = DrawdownEngine()

    def build(self):

        return {

            "statistics": self.statistics.build(),

            "metrics": self.metrics.build(),

            "equity_curve": self.equity.build(),

            "drawdown": self.drawdown.build()

        }