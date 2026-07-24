from app.execution.brokers.oanda_broker import OandaBroker

broker = OandaBroker()

print()

print("Connected:", broker.is_connected())

broker.connect()

print("Connected:", broker.is_connected())

print()

order = {

    "symbol": "GBPUSD",

    "direction": "SELL",

    "quantity": 0.50

}

print(broker.place_order(order))

broker.disconnect()

print()

print("Connected:", broker.is_connected())