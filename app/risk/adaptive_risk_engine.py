
from app.ai.memory.performance_engine import PerformanceEngine


class AdaptiveRiskEngine:

    def __init__(self):

        self.performance = PerformanceEngine()

    def calculate(self, base_risk):

        stats = self.performance.build()

        if stats["total"] < 10:

            return base_risk

        win_rate = stats["win_rate"]

        if win_rate >= 70:

            multiplier = 1.50

        elif win_rate >= 60:

            multiplier = 1.20

        elif win_rate >= 50:

            multiplier = 1.00

        elif win_rate >= 40:

            multiplier = 0.75

        else:

            multiplier = 0.50

        return round(
            base_risk * multiplier,
            2
        )