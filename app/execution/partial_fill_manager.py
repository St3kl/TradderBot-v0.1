class PartialFillManager:

    def update(

        self,

        order,

        filled_quantity,

    ):

        order.setdefault("filled", 0.0)

        order["filled"] += filled_quantity

        total = order["quantity"]

        if order["filled"] >= total:

            order["filled"] = total

            order["status"] = "FILLED"

        else:

            order["status"] = "PARTIAL"

        return order

    def remaining(self, order):

        return round(

            order["quantity"] - order["filled"],

            8

        )

    def print(self, order):

        print()

        print("=" * 60)

        print("PARTIAL FILL")

        print("=" * 60)

        print()

        print("Quantity :", order["quantity"])

        print("Filled   :", order["filled"])

        print("Remaining:", self.remaining(order))

        print("Status   :", order["status"])