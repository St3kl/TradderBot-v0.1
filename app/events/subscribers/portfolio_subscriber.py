from app.logger.logger import Logger

logger = Logger.get("PortfolioSubscriber")


class PortfolioSubscriber:

    def __init__(self, portfolio):

        self.portfolio = portfolio

    def on_trade_executed(self, event):

        logger.info(

            f"Updating portfolio for {event.symbol}"

        )

        trade = {

            "symbol": event.symbol,

            "side": event.side,

            "entry": event.entry,

            "stop_loss": event.stop_loss,

            "take_profit": event.take_profit,

            "confidence": event.confidence

        }

        self.portfolio.update(trade)