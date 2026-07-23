from datetime import datetime


class OrderCancellation:

    def cancel(

        self,

        order,

        reason="",

    ):

        order["status"] = "CANCELLED"

        order["cancelled"] = True

        order["cancel_reason"] = reason

        order["cancelled_at"] = datetime.utcnow()

        return order

    def cancelled(self, order):

        return order.get("cancelled", False)

    def print(self, order):

        print()

        print("=" * 60)

        print("ORDER CANCELLATION")

        print("=" * 60)

        print()

        print("ID      :", order["id"])

        print("Status  :", order["status"])

        print("Reason  :", order["cancel_reason"])

        print("Time    :", order["cancelled_at"])