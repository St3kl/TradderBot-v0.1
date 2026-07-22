from datetime import datetime

from app.core.events.event_bus import EventBus
from app.events.event_types import TradeExecuted


bus = EventBus()


def learning_listener(event):

    print()

    print("Learning received")

    print(event.symbol)

    print(event.entry)


def journal_listener(event):

    print()

    print("Journal received")

    print(event.side)


bus.subscribe(
    TradeExecuted,
    learning_listener
)

bus.subscribe(
    TradeExecuted,
    journal_listener
)

bus.publish(

    TradeExecuted(

        symbol="BTCUSDT",

        side="LONG",

        entry=62000,

        stop_loss=61500,

        take_profit=63000,

        confidence=92,

        timestamp=datetime.now()

    )

)

print()

print("✓ TEST PASSED")