class PerformanceDashboard:

    def build(
        self,
        portfolio,
        analytics,
        trade_quality,
        market_health,
        rejection_stats,
    ):

        return {

            "portfolio": portfolio,

            "analytics": analytics,

            "trade_quality": trade_quality,

            "market_health": market_health,

            "rejections": rejection_stats,

        }

    def print(self, dashboard):

        print()

        print("=" * 60)
        print("PERFORMANCE DASHBOARD")
        print("=" * 60)

        print()

        print("Portfolio")

        for k, v in dashboard["portfolio"].items():
            print(f"{k:<20} {v}")

        print()

        print("Analytics")

        print(dashboard["analytics"])

        print()

        print("Trade Quality")

        print(dashboard["trade_quality"])

        print()

        print("Market Health")

        print(dashboard["market_health"])

        print()

        print("Rejection Statistics")

        print(dashboard["rejections"])