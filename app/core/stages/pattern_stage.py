from app.market.patterns.detector import detect_pattern
from app.market.patterns.support_resistance import find_support_resistance


class PatternStage:

    def run(self, session):

        print("Running Pattern Stage")

        # session.pattern = detect_pattern(
        #     session.indicators
        # )
        pattern = detect_pattern(session.indicators)

        session.patterns["primary"] = pattern
        session.patterns["detected"] = [pattern]
        session.patterns["confidence"] = pattern.get("confidence", 50) if isinstance(pattern, dict) else 50

        # compatibility
        session.pattern = session.patterns

        return session