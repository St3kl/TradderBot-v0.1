from app.paper.trade_monitor import TradeMonitor
from app.core.events import dispatcher
from app.events.trade_events import TRADE_CLOSED


monitor = TradeMonitor()

monitor.monitor(
    current_price=64100
)



def on_trade_closed(trade):

    print()

    print("EVENT RECEIVED")

    print(trade["symbol"])

    print(trade["result"])

    print(trade["pnl"])

    print()


dispatcher.subscribe(
    TRADE_CLOSED,
    on_trade_closed
)

monitor = TradeMonitor()

monitor.monitor(
    current_price=64100
)