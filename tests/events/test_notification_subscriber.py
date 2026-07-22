from datetime import datetime

from app.application import Application

from app.events.event_types import TradeExecuted


print()
print("=" * 40)
print("NOTIFICATION SUBSCRIBER")
print("=" * 40)

app = Application()

event = TradeExecuted(

    symbol="BTCUSDT",

    side="BUY",

    entry=45000,

    stop_loss=44500,

    take_profit=47000,

    confidence=92,

    strategy="TREND",

    regime="TRENDING",

    volatility="HIGH",

    timestamp=datetime.now()

)

app.container.event_bus().publish(event)

print()
print("✓ TEST PASSED")