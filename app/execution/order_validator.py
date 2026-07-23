class OrderValidator:

    def validate(self, order):

        errors = []

        if not order.get("symbol"):
            errors.append("Missing symbol")

        if order.get("direction") not in ["BUY", "SELL"]:
            errors.append("Invalid direction")

        if order.get("entry", 0) <= 0:
            errors.append("Invalid entry price")

        if order.get("stop_loss", 0) <= 0:
            errors.append("Invalid stop loss")

        if order.get("take_profit", 0) <= 0:
            errors.append("Invalid take profit")

        if order.get("lot_size", 0) <= 0:
            errors.append("Invalid lot size")

        if order.get("risk_percent", 0) <= 0:
            errors.append("Invalid risk percent")

        return {

            "valid": len(errors) == 0,

            "errors": errors

        }

    def print(self, report):

        print()

        print("=" * 60)
        print("ORDER VALIDATION")
        print("=" * 60)
        print()

        print("Valid :", report["valid"])

        if report["errors"]:

            print()

            print("Errors")

            for error in report["errors"]:

                print("-", error)