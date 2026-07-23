class OrderStatusManager:

    VALID_STATUSES = {

        "CREATED",

        "VALIDATED",

        "SUBMITTED",

        "PENDING",

        "FILLED",

        "PARTIAL",

        "MODIFIED",

        "CANCELLED",

        "REJECTED",

        "CLOSED",

    }

    def update(self, order, status):

        if status not in self.VALID_STATUSES:

            raise ValueError(

                f"Invalid status: {status}"

            )

        order["status"] = status

        return order

    def get(self, order):

        return order.get("status", "UNKNOWN")

    def print(self, order):

        print()

        print("=" * 60)

        print("ORDER STATUS")

        print("=" * 60)

        print()

        print("ID     :", order["id"])

        print("Status :", order["status"])