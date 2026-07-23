from app.execution.brokers.mock_broker import MockBroker

broker = MockBroker()

print("Connected:", broker.is_connected())

broker.connect()

print("Connected:", broker.is_connected())

print()

print("Balance:", broker.get_balance())

print()

print(

    broker.place_order(

        {

            "symbol": "BTCUSDT"

        }

    )

)