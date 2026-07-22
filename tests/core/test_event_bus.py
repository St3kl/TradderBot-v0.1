from app.core.events.event_bus import EventBus

from app.core.events.events import TRADE_CLOSED

bus = EventBus()


def learning(data):

    print(

        "Learning:",

        data

    )


def portfolio(data):

    print(

        "Portfolio:",

        data

    )


bus.subscribe(

    TRADE_CLOSED,

    learning

)

bus.subscribe(

    TRADE_CLOSED,

    portfolio

)

print()

print("="*40)

print("EVENT BUS")

print("="*40)

print()

bus.publish(

    TRADE_CLOSED,

    {

        "symbol":"BTCUSDT",

        "pnl":250

    }

)

print()

print("✓ TEST PASSED")