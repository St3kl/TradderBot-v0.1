from pprint import pprint


class ReportGenerator:
    """
    Builds the final backtest report.
    """

    def generate(

        self,

        portfolio,

        performance,

        strategy_stats=None,

        market_stats=None,

        learning=None

    ):

        report = {

    "portfolio": portfolio,

    "performance": performance,

    "strategy_statistics": strategy_stats or {},

    "market_statistics": market_stats or {},

    "learning": learning or {}

}

        return report

    def print(self, report):

        print()

        print("=" * 60)

        print("FINAL BACKTEST REPORT")

        print("=" * 60)

        print()

        pprint(report)

        print()