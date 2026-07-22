class ReplayReview:

    """
    Reviews a completed pipeline session and explains
    why a trade was accepted or rejected.
    """

    def review(self, session):

        decision = session.decision

        confluence = session.confluence

        validation = session.validation

        checklist = session.checklist

        return {

            "decision": decision.get("action", "WAIT"),

            "reason": decision.get("reason", ""),

            "confidence": decision.get("confidence", 0),

            "confluence_score": confluence.get("score", 0),

            "validation_score": validation.get("score", 0),

            "missing": confluence.get("missing", []),

            "signals": confluence.get("signals", []),

            "failed_checklist": [

                name

                for name, passed in checklist.items()

                if not passed

            ],

            "passed_checklist": [

                name

                for name, passed in checklist.items()

                if passed

            ]

        }