class UnrealizedPnLEngine:

    def calculate(self, position, current_price):

        entry = position["entry"]

        qty = position["quantity"]

        direction = position["direction"]

        if direction == "LONG":

            pnl = (current_price - entry) * qty

        else:

            pnl = (entry - current_price) * qty

        return {

            "broker_order_id": position["broker_order_id"],

            "entry": entry,

            "current_price": current_price,

            "quantity": qty,

            "direction": direction,

            "unrealized_pnl": round(pnl, 2)

        }

    def print(self, report):

        print()

        print("=" * 60)

        print("UNREALIZED PNL")

        print("=" * 60)

        print()

        print("Entry     :", report["entry"])

        print("Current   :", report["current_price"])

        print("Direction :", report["direction"])

        print("Quantity  :", report["quantity"])

        print("PnL       :", report["unrealized_pnl"])