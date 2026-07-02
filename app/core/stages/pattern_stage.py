from app.patterns.detector import detect_pattern


class PatternStage:

    def run(self, session):

        print("Running Pattern Stage")

        session.pattern = detect_pattern(
            session.indicators
        )

        return session