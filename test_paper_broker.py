from app.paper.paper_broker import PaperBroker
from app.models.trade_plan import TradePlan

broker = PaperBroker()

trade = TradePlan()

trade.entry = 100

trade.position_size = 2

trade.direction = "BUY"

closed = broker.close_trade(
    trade,
    exit_price=110,
    result="TP"
)

print(closed.pnl)