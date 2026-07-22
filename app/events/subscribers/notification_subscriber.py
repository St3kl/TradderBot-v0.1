from app.logger.logger import Logger

logger = Logger.get("NotificationSubscriber")


class NotificationSubscriber:
    """
    Receives TradeExecuted events and sends notifications.

    Currently logs the notification.

    Later this can send:
        - Telegram
        - Discord
        - Email
        - Slack
        - WhatsApp
    """

    def on_trade_executed(self, event):

        logger.info(

            f"Trade Executed | "

            f"{event.symbol} "

            f"{event.side} "

            f"Entry={event.entry}"

        )