class BrokerHealthMonitor:

    def evaluate(

        self,

        connected,

        latency_ms,

        slippage,

        retries

    ):

        score = 100

        if not connected:
            score -= 50

        if latency_ms > 300:
            score -= 20

        elif latency_ms > 150:
            score -= 10

        if abs(slippage) > 20:
            score -= 20

        elif abs(slippage) > 10:
            score -= 10

        score -= retries * 5

        score = max(0, score)

        if score >= 90:
            status = "EXCELLENT"

        elif score >= 75:
            status = "GOOD"

        elif score >= 60:
            status = "FAIR"

        else:
            status = "POOR"

        return {

            "score": score,

            "status": status

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("BROKER HEALTH")

        print("=" * 60)

        print()

        print("Score  :", report["score"])

        print("Status :", report["status"])