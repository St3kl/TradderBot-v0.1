class ConfidenceCalibrator:

    def calibrate(self, trades):

        buckets = {}

        for trade in trades:

            confidence = trade.get("confidence", 0)

            bucket = int(confidence / 10) * 10

            if bucket not in buckets:

                buckets[bucket] = {

                    "wins": 0,

                    "losses": 0,

                    "total": 0

                }

            buckets[bucket]["total"] += 1

            if trade["result"] == "WIN":

                buckets[bucket]["wins"] += 1

            else:

                buckets[bucket]["losses"] += 1

        report = {}

        for bucket, stats in buckets.items():

            actual = round(

                stats["wins"] /

                stats["total"] * 100,

                2

            )

            report[bucket] = {

                "predicted": bucket,

                "actual": actual,

                "difference": round(actual - bucket, 2),

                "total": stats["total"]

            }

        return report

    def print(self, report):

        print()

        print("=" * 60)

        print("CONFIDENCE CALIBRATION")

        print("=" * 60)

        print()

        for bucket in sorted(report):

            row = report[bucket]

            print(

                f"{bucket:>2}%"

                f" -> Actual {row['actual']}%"

                f" Difference {row['difference']}"

            )
            