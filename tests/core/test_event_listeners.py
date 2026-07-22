from app.core.events.event_bus import EventBus
from app.core.events.events import TRADE_CLOSED

from app.core.events.listeners.logger_listener import LoggerListener


bus = EventBus()

logger = LoggerListener()

bus.subscribe(

    TRADE_CLOSED,

    logger.handle

)

print()

print("=" * 40)

print("EVENT LISTENERS")

print("=" * 40)

print()

bus.publish(

    TRADE_CLOSED,

    {

        "symbol":"BTCUSDT",

        "pnl":150

    }

)

print()

print("✓ TEST PASSED")