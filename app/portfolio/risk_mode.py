class RiskMode:

    def evaluate(self, portfolio_risk_score):

        score = portfolio_risk_score["score"]

        if score >= 90:

            mode = "AGGRESSIVE"

        elif score >= 70:

            mode = "NORMAL"

        elif score >= 50:

            mode = "DEFENSIVE"

        else:

            mode = "SURVIVAL"

        return {

            "mode": mode,

            "risk_score": score

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("RISK MODE")

        print("=" * 60)

        print()

        print("Mode       :", report["mode"])

        print("Risk Score :", report["risk_score"])