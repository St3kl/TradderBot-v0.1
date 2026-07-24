from app.execution.brokers.binance_broker import BinanceBroker

broker = BinanceBroker()

print()

print("Connected:", broker.is_connected())

broker.connect()

print("Connected:", broker.is_connected())

print()

order = {

    "symbol": "BTCUSDT",

    "direction": "BUY",

    "quantity": 0.01

}

print(broker.place_order(order))

broker.disconnect()

print()

print("Connected:", broker.is_connected())