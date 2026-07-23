class PortfolioRiskScore:

    def calculate(

        self,

        concentration_ok,

        correlation_ok,

        heat_ok,

        drawdown_ok,

        diversification_score

    ):

        score = 100

        if not concentration_ok:
            score -= 20

        if not correlation_ok:
            score -= 20

        if not heat_ok:
            score -= 20

        if not drawdown_ok:
            score -= 20

        score *= diversification_score / 100

        if score >= 90:

            level = "LOW"

        elif score >= 70:

            level = "MODERATE"

        elif score >= 50:

            level = "HIGH"

        else:

            level = "CRITICAL"

        return {

            "score": round(score, 2),

            "level": level

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("PORTFOLIO RISK SCORE")

        print("=" * 60)

        print()

        print("Risk Score :", report["score"])

        print("Risk Level :", report["level"])