class OrderRouter:

    def __init__(self):

        self.brokers = {}

    def register(self, name, broker):

        self.brokers[name] = broker

    def route(self, broker_name):

        if broker_name not in self.brokers:

            raise ValueError(

                f"Unknown broker: {broker_name}"

            )

        return self.brokers[broker_name]

    def available_brokers(self):

        return list(self.brokers.keys())

    def print(self):

        print()

        print("=" * 60)

        print("ORDER ROUTER")

        print("=" * 60)

        print()

        for broker in self.available_brokers():

            print(broker)