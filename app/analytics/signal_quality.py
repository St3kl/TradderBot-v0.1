class SignalQuality:

    def analyze(self, trades):

        buckets = {}

        for trade in trades:

            confidence = trade.get("confidence", 0)

            bucket = int(confidence // 10) * 10

            if bucket not in buckets:
                buckets[bucket] = {
                    "total": 0,
                    "wins": 0,
                    "losses": 0,
                }

            buckets[bucket]["total"] += 1

            if trade.get("result") == "WIN":
                buckets[bucket]["wins"] += 1
            elif trade.get("result") == "LOSS":
                buckets[bucket]["losses"] += 1

        for bucket in buckets.values():

            total = bucket["total"]

            bucket["win_rate"] = (
                round(bucket["wins"] / total * 100, 2)
                if total
                else 0
            )

        return dict(sorted(buckets.items()))