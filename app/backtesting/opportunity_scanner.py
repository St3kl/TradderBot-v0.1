class OpportunityScanner:
    """
    Tracks every trading opportunity during a backtest.
    """

    def __init__(self):

        self.valid = []

        self.rejected = []

    def scan(self, session):

        decision = session.decision.get("action", "WAIT")

        record = {
            "time": session.replay.candle["time"],
            "symbol": session.symbol,
            "strategy": getattr(session, "strategy", "DEFAULT"),
            "confidence": session.decision.get("confidence", 0),
            "reason": session.decision.get("reason", ""),
        }

        if decision == "WAIT":

            self.rejected.append(record)

        else:

            record["direction"] = decision

            self.valid.append(record)

    def summary(self):

        return {

            "valid": len(self.valid),

            "rejected": len(self.rejected),

            "total": len(self.valid) + len(self.rejected),

        }

    def by_strategy(self):

        ranking = {}

        for trade in self.valid:

            s = trade["strategy"]

            ranking.setdefault(s, 0)

            ranking[s] += 1

        return ranking

    def top_rejections(self):

        reasons = {}

        for trade in self.rejected:

            r = trade["reason"]

            reasons.setdefault(r, 0)

            reasons[r] += 1

        return dict(

            sorted(

                reasons.items(),

                key=lambda x: x[1],

                reverse=True,

            )

        )