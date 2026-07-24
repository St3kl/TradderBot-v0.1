from datetime import datetime


class PaperBroker:

    def __init__(self, starting_balance=100000):

        self.connected = True

        self.balance = starting_balance

        self.positions = []

        self.order_counter = 1

    def connect(self):
        self.connected = True
        return True

    def disconnect(self):
        self.connected = False

    def is_connected(self):
        return self.connected

    def get_balance(self):
        return self.balance

    def get_positions(self):
        return self.positions

    def place_order(self, order):

        broker_order_id = f"PAPER-{self.order_counter:06d}"

        self.order_counter += 1

        position = {
            "broker_order_id": broker_order_id,
            "symbol": order["symbol"],
            "direction": order["direction"],
            "entry": order["entry"],
            "quantity": order["quantity"],
            "opened_at": datetime.utcnow(),
            "status": "OPEN"
        }

        self.positions.append(position)

        return {
            "success": True,
            "broker_order_id": broker_order_id
        }

    def close_position(self, broker_order_id):

        for position in self.positions:

            if position["broker_order_id"] == broker_order_id:

                position["status"] = "CLOSED"

                position["closed_at"] = datetime.utcnow()

                return True

        return False