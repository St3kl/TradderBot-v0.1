from app.execution.brokers.mt5_broker import MT5Broker

broker = MT5Broker()

print()

print("Connected:", broker.is_connected())

broker.connect()

print("Connected:", broker.is_connected())

print()

order = {

    "symbol": "EURUSD",

    "direction": "BUY",

    "quantity": 0.10

}

print(broker.place_order(order))

broker.disconnect()

print()

print("Connected:", broker.is_connected())