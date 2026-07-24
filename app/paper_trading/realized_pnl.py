class RealizedPnLEngine:

    def calculate(self, position, exit_price):

        entry = position["entry"]
        qty = position["quantity"]
        direction = position["direction"]

        if direction == "LONG":
            pnl = (exit_price - entry) * qty
        else:
            pnl = (entry - exit_price) * qty

        return {
            "broker_order_id": position["broker_order_id"],
            "entry": entry,
            "exit": exit_price,
            "quantity": qty,
            "direction": direction,
            "realized_pnl": round(pnl, 2)
        }

    def print(self, report):

        print()
        print("=" * 60)
        print("REALIZED PNL")
        print("=" * 60)
        print()

        print("Entry      :", report["entry"])
        print("Exit       :", report["exit"])
        print("Direction  :", report["direction"])
        print("Quantity   :", report["quantity"])
        print("Realized   :", report["realized_pnl"])