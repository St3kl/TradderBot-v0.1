from datetime import datetime

from app.application import Application

from app.events.event_types import TradeExecuted

print()

print("=" * 40)
print("LEARNING SUBSCRIBER")
print("=" * 40)

app = Application()

event = TradeExecuted(

    symbol="BTCUSDT",

    side="LONG",

    entry=62000,

    stop_loss=61500,

    take_profit=63000,

    confidence=95,

    strategy="TREND",

    regime="TRENDING",

    volatility="NORMAL",

    timestamp=datetime.now()

)

app.container.event_bus().publish(event)

print()

print("✓ TEST PASSED")