from app.core.events.events import TRADE_CLOSED

from app.core.events.listeners.logger_listener import LoggerListener


class EventRegistry:
    """
    Automatically registers all event listeners.
    """

    def __init__(self, bus):

        self.bus = bus

    def register(self):

        logger = LoggerListener()

        self.bus.subscribe(

            TRADE_CLOSED,

            logger.handle

        )

        print("✓ Event listeners registered")