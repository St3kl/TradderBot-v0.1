from app.core.events import dispatcher
from app.events.trade_events import TRADE_CLOSED


def listener(trade):

    print()

    print("EVENT RECEIVED")

    print(trade["symbol"])

    print()


dispatcher.subscribe(

    TRADE_CLOSED,

    listener

)

dispatcher.dispatch(

    TRADE_CLOSED,

    {

        "symbol": "BTCUSDT"

    }

)