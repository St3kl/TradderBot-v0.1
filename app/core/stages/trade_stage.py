# from app.risk.calculator import calculate_trade_levels


# class TradeStage:

#     def run(self, session):

#         print("Running Trade Stage")

#         session.trade = calculate_trade_levels(
#             price=session.indicators["price"],
#             support=session.sr["support"],
#             resistance=session.sr["resistance"],
#             bullish=session.bullish,
#             atr=session.indicators["atr"]
#         )

#         print("Trade:", session.trade)

#         return session

from app.core.events import dispatcher
from app.events.trade_events import TRADE_CLOSED


def on_trade_closed(trade):

    print()

    print("EVENT RECEIVED")

    print(trade)

    print()


dispatcher.subscribe(
    TRADE_CLOSED,
    on_trade_closed
)

dispatcher.dispatch(
    TRADE_CLOSED,
    {
        "symbol": "BTCUSDT",
        "result": "WIN"
    }
)