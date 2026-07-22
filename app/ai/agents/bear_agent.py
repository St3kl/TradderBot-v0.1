class BearAgent:
    """
    Evaluates bearish evidence.
    """

    def evaluate(self, session):

        score = 0

        if session.bearish:

            score += 50

        if session.downtrend:

            score += 30

        if session.sell_volume:

            score += 20

        return {

            "agent": "Bear",

            "score": score

        }