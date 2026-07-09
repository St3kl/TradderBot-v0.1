from app.backtesting.trade_manager import TradeManager

manager = TradeManager()

trade = {

    "id": 1,

    "symbol": "BTCUSDT"

}

manager.add(trade)

print(manager.total_open())

manager.close(trade)

print(manager.total_open())

print(manager.total_closed())