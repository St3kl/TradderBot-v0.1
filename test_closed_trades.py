from app.database.repositories.trade_repository import TradeRepository

repo = TradeRepository()

for trade in repo.get_closed_trades():

    print(trade)