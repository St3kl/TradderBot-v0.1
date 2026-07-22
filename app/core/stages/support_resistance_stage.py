from app.market.patterns.support_resistance import find_support_resistance


class SupportResistanceStage:

    def run(self, session):

        print("Running Support/Resistance Stage")

        closes = [c["close"] for c in session.replay.dataset]

        levels = find_support_resistance(closes)

        session.sr.update(levels)

        return session