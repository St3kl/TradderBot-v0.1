from app.core.session import TradingSession


class SessionFactory:
    """
    Creates TradingSession objects for tests.
    """

    @staticmethod
    def create(**overrides):

        session = TradingSession()

        session.symbol = "BTCUSDT"

        session.strategy = "DEFAULT"

        session.market_regime = {

            "regime": "TRANSITION",

            "volatility": "NORMAL"

        }

        session.bullish = True

        session.trade = {

            "entry": 62000,

            "stop_loss": 61500,

            "take_profit": 63000,

            "risk_reward": 2.0

        }

        session.decision = {

            "action": "BUY",

            "confidence": 65

        }

        # Allow overriding any attribute
        for key, value in overrides.items():

            setattr(session, key, value)

        return session