class PortfolioGovernor:

    def approve(

        self,

        risk_mode,

        strategy_health,

        portfolio_risk,

        trading_window,

    ):

        reasons = []

        approved = True

        if risk_mode["mode"] == "SURVIVAL":

            approved = False

            reasons.append(

                "Portfolio in Survival Mode"

            )

        if strategy_health["status"] == "CRITICAL":

            approved = False

            reasons.append(

                "Strategy Critical"

            )

        if portfolio_risk["level"] == "CRITICAL":

            approved = False

            reasons.append(

                "Portfolio Risk Critical"

            )

        if not trading_window["allowed"]:

            approved = False

            reasons.extend(

                trading_window["reasons"]

            )

        return {

            "approved": approved,

            "reasons": reasons

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("PORTFOLIO GOVERNOR")

        print("=" * 60)

        print()

        print("Approved :", report["approved"])

        print()

        if report["reasons"]:

            print("Reasons")

            for reason in report["reasons"]:

                print("-", reason)