from app.market.market_data_manager import MarketDataManager

manager = MarketDataManager()

manager.update_price("BTCUSDT", 65120.5)
manager.update_price("ETHUSDT", 3524.8)
manager.update_price("EURUSD", 1.1734)

manager.print()

print()

print(manager.get_price("BTCUSDT"))

print()

print(manager.symbols())