class ChiefAgent:
    """
    Aggregates every AI agent into
    one final decision.
    """

    def decide(self, reports):

        total = 0

        reasons = []

        for report in reports:

            total += report["score"]

            reasons.extend(

                report.get(

                    "reasons",

                    []

                )

            )

        confidence = round(

            total / len(reports)

        )

        if confidence >= 75:

            decision = "BUY"

        elif confidence >= 50:

            decision = "HOLD"

        else:

            decision = "SELL"

        return {

            "decision": decision,

            "confidence": confidence,

            "reports": reports,

            "reasons": reasons

        }