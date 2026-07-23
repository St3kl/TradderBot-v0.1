class ConcentrationRisk:

    def evaluate(self, diversification, limit=40):

        alerts = []

        for asset, exposure in diversification["assets"].items():

            if exposure > limit:

                alerts.append({

                    "asset": asset,

                    "exposure": exposure,

                    "warning": "Exposure Limit Exceeded"

                })

        return {

            "healthy": len(alerts) == 0,

            "alerts": alerts

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("CONCENTRATION RISK")

        print("=" * 60)

        print()

        if report["healthy"]:

            print("Portfolio is well diversified.")

            return

        for alert in report["alerts"]:

            print(

                f"{alert['asset']:<10}"

                f"{alert['exposure']}%"

                f" -> {alert['warning']}"

            )