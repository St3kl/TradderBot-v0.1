from app.execution.brokers.paper_broker import PaperBroker

broker = PaperBroker()

print()

print("Balance")

print(broker.get_balance())

print()

report = broker.place_order({

    "symbol": "BTCUSDT",

    "direction": "LONG",

    "entry": 65000,

    "quantity": 0.02

})

print(report)

print()

print("Positions")

for position in broker.get_positions():

    print(position)

print()

broker.close_position(

    report["broker_order_id"]

)

print("After Closing")

for position in broker.get_positions():

    print(position)