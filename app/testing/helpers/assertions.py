class Assertions:
    """
    Common assertions used by tests.
    """

    @staticmethod
    def valid_trade(trade):

        assert trade is not None

        assert trade["symbol"]

        assert trade["strategy"]

        assert trade["confidence"] >= 0

    @staticmethod
    def valid_session(session):

        assert session.symbol != ""

        assert session.strategy is not None

    @staticmethod
    def valid_execution(execution):

        assert "execute" in execution

        assert "risk" in execution