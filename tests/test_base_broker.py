from app.execution.brokers.mock_broker import MockBroker

broker = MockBroker()

print()

print("Implements:")

print(hasattr(broker, "connect"))
print(hasattr(broker, "disconnect"))
print(hasattr(broker, "get_balance"))
print(hasattr(broker, "place_order"))
print(hasattr(broker, "close_position"))