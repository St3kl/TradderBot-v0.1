from app.patterns.support_resistance import find_support_resistance


class SupportResistanceStage:

    def run(self, session):

        print("Running Support/Resistance Stage")

        levels = find_support_resistance(
            session.indicators["closes"]
        )

        session.sr.update(levels)

        return session