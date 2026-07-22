from app.core.events.event_bus import EventBus
from app.core.events.event_registry import EventRegistry

from app.core.events.events import TRADE_CLOSED

bus = EventBus()

registry = EventRegistry(bus)

registry.register()

print()

print("=" * 40)

print("EVENT REGISTRY")

print("=" * 40)

print()

bus.publish(

    TRADE_CLOSED,

    {

        "symbol": "BTCUSDT",

        "pnl": 500

    }

)

print()

print("✓ TEST PASSED")