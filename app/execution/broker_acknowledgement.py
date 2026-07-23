class BrokerAcknowledgement:

    def acknowledge(

        self,

        order,

        broker_order_id,

        broker_name,

    ):

        order["broker_order_id"] = broker_order_id

        order["broker"] = broker_name

        order["acknowledged"] = True

        return order

    def acknowledged(self, order):

        return order.get("acknowledged", False)

    def print(self, order):

        print()

        print("=" * 60)
        print("BROKER ACKNOWLEDGEMENT")
        print("=" * 60)
        print()

        print("Internal ID :", order["id"])
        print("Broker      :", order["broker"])
        print("Broker ID   :", order["broker_order_id"])
        print("ACK         :", order["acknowledged"])