class CorrelatedExposure:

    def evaluate(self, positions, correlations, threshold=0.80):

        alerts = []

        for i in range(len(positions)):

            for j in range(i + 1, len(positions)):

                a = positions[i]["symbol"]
                b = positions[j]["symbol"]

                key = tuple(sorted([a, b]))

                corr = correlations.get(key, 0)

                if corr >= threshold:

                    alerts.append({

                        "asset1": a,

                        "asset2": b,

                        "correlation": corr

                    })

        return {

            "healthy": len(alerts) == 0,

            "alerts": alerts

        }

    def print(self, report):

        print()

        print("=" * 60)
        print("CORRELATED EXPOSURE")
        print("=" * 60)
        print()

        if report["healthy"]:

            print("No excessive correlation detected.")

            return

        for alert in report["alerts"]:

            print(

                f"{alert['asset1']} <-> "

                f"{alert['asset2']} "

                f"({alert['correlation']})"

            )