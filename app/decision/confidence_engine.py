class ConfidenceEngine:
    """
    Converts every module into one probability score.
    """

    def calculate(self, session):

        scores = []

        scores.append(session.confluence["confidence"])
        scores.append(session.validation["confidence"])
        scores.append(session.trend["confidence"])

        if hasattr(session, "ai"):

            if "confidence" in session.ai:

                scores.append(session.ai["confidence"])

        confidence = sum(scores) / len(scores)

        return round(confidence, 2)