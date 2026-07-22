from app.analytics.winrate_analyzer import WinrateAnalyzer
from app.analytics.expectancy import ExpectancyAnalyzer


class AnalyticsEngine:

    def __init__(self):

        self.winrate = WinrateAnalyzer()

        self.expectancy = ExpectancyAnalyzer()

    def analyze(self, trades):

        return {

            "winrate": self.winrate.analyze(trades),

            "expectancy": self.expectancy.analyze(trades)

        }