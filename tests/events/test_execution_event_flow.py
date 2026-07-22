from datetime import datetime

from app.core.events.event_bus import EventBus
from app.events.event_types import TradeExecuted

bus = EventBus()


class Learning:

    def learn(self, trade):

        print()

        print("Learning")

        print(trade)


learning = Learning()


class LearningSubscriber:

    def __init__(self, learning):

        self.learning = learning

    def on_trade_executed(self, event):

        self.learning.learn({

            "symbol": event.symbol,

            "confidence": event.confidence

        })


subscriber = LearningSubscriber(learning)

bus.subscribe(

    TradeExecuted,

    subscriber.on_trade_executed

)

bus.publish(

    TradeExecuted(

        symbol="BTCUSDT",

        side="LONG",

        entry=62000,

        stop_loss=61500,

        take_profit=63000,

        confidence=93,

        timestamp=datetime.now()

    )

)

print()

print("✓ TEST PASSED")