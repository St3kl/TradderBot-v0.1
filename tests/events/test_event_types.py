from datetime import datetime

from app.events.event_types import TradeExecuted

print()

print("=" * 40)
print("EVENT TYPES")
print("=" * 40)

event = TradeExecuted(

    symbol="BTCUSDT",

    side="LONG",

    entry=62000,

    stop_loss=61500,

    take_profit=63000,

    confidence=91,

    timestamp=datetime.now()

)

print(event)

print()

print("✓ TEST PASSED")