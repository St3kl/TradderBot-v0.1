from app.logger.logger import Logger

logger = Logger.get("JournalSubscriber")


class JournalSubscriber:

    def __init__(self, journal):

        self.journal = journal

    def on_trade_executed(self, event):

        logger.info(

            f"Saving trade {event.symbol}"

        )

        trade = {

            "symbol": event.symbol,

            "side": event.side,

            "entry": event.entry,

            "stop_loss": event.stop_loss,

            "take_profit": event.take_profit,

            "confidence": event.confidence,

            "strategy": event.strategy,

            "regime": event.regime,

            "volatility": event.volatility,

            "timestamp": event.timestamp

        }

        self.journal.save(trade)