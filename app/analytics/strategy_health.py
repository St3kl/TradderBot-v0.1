class StrategyHealth:

    def evaluate(self, strategy):

        score = strategy.get("score", 0)

        expectancy = strategy.get("expectancy", 0)

        recovery = strategy.get("recovery_factor", 0)

        if score >= 90 and expectancy > 0 and recovery > 3:

            status = "EXCELLENT"

        elif score >= 80:

            status = "HEALTHY"

        elif score >= 70:

            status = "STABLE"

        elif score >= 60:

            status = "WARNING"

        else:

            status = "CRITICAL"

        return {

            "status": status,

            "score": score,

            "expectancy": expectancy,

            "recovery_factor": recovery

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("STRATEGY HEALTH")

        print("=" * 60)

        print()

        print("Status           :", report["status"])

        print("Score            :", report["score"])

        print("Expectancy       :", report["expectancy"])

        print("Recovery Factor  :", report["recovery_factor"])