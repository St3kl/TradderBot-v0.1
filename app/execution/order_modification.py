from datetime import datetime


class OrderModification:

    def modify(

        self,

        order,

        **changes

    ):

        order.setdefault("modifications", [])

        record = {

            "time": datetime.utcnow(),

            "changes": changes.copy()

        }

        order["modifications"].append(record)

        for key, value in changes.items():

            order[key] = value

        order["status"] = "MODIFIED"

        return order

    def history(self, order):

        return order.get("modifications", [])

    def print(self, order):

        print()

        print("=" * 60)
        print("ORDER MODIFICATION")
        print("=" * 60)
        print()

        print("ID :", order["id"])
        print("Status :", order["status"])

        print()

        print("Current Values")

        for key in [

            "entry",

            "stop_loss",

            "take_profit",

            "quantity"

        ]:

            if key in order:

                print(f"{key:<12}: {order[key]}")

        print()

        print("Modification History")

        for item in self.history(order):

            print(item["time"], item["changes"])