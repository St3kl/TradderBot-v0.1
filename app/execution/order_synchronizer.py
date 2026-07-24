class OrderSynchronizer:

    def __init__(self):

        self.orders = {}

    def synchronize(self, broker_orders):

        self.orders = {}

        for order in broker_orders:

            self.orders[order["broker_order_id"]] = order

        return self.orders

    def get_order(self, broker_order_id):

        return self.orders.get(broker_order_id)

    def count(self):

        return len(self.orders)

    def print(self):

        print()

        print("=" * 60)
        print("ORDER SYNCHRONIZATION")
        print("=" * 60)
        print()

        print("Orders :", self.count())

        print()

        for order in self.orders.values():

            print(

                order["broker_order_id"],

                order["symbol"],

                order["status"]

            )