from app.logger.logger import Logger

logger = Logger.get("LearningSubscriber")


class LearningSubscriber:

    def __init__(self, learning_engine):

        self.learning = learning_engine

    def on_trade_executed(self, event):

        logger.info(

            f"Learning from {event.symbol}"

        )

        trade = {

    "symbol": event.symbol,

    "side": event.side,

    "strategy": event.strategy,

    "regime": event.regime,

    "volatility": event.volatility,

    "entry": event.entry,

    "confidence": event.confidence,

}

        self.learning.learn(trade)