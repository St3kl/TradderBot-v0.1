from app.execution.brokers.broker_factory import BrokerFactory

for broker_name in [

    "mock",

    "binance",

    "mt5",

    "oanda"

]:

    broker = BrokerFactory.create(broker_name)

    print()

    print(

        broker_name,

        "->",

        broker.__class__.__name__

    )

print()

try:

    BrokerFactory.create("kraken")

except Exception as e:

    print(e)