class BullAgent:
    """
    Evaluates bullish evidence.
    """

    def evaluate(self, session):

        score = 0

        if session.bullish:

            score += 50

        if session.trend:

            score += 30

        if session.volume:

            score += 20

        return {

            "agent": "Bull",

            "score": score

        }