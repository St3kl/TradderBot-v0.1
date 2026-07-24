class ProductionReadinessValidator:

    def validate(
        self,
        kill_switch_active,
        circuit_open,
        health_score,
        production_mode_live,
        broker_connected
    ):

        reasons = []

        if kill_switch_active:
            reasons.append("Emergency Kill Switch Active")

        if circuit_open:
            reasons.append("Circuit Breaker Open")

        if health_score < 80:
            reasons.append("System Health Too Low")

        if not production_mode_live:
            reasons.append("Not In LIVE Mode")

        if not broker_connected:
            reasons.append("Broker Disconnected")

        return {

            "ready": len(reasons) == 0,

            "reasons": reasons

        }

    def print(self, result):

        print()
        print("=" * 60)
        print("PRODUCTION READINESS")
        print("=" * 60)
        print()

        print("Ready :", result["ready"])

        if result["reasons"]:

            print()
            print("Reasons")

            for reason in result["reasons"]:
                print("-", reason)