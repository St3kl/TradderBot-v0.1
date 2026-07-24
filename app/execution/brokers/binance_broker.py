from app.execution.brokers.base_broker import BaseBroker


class BinanceBroker(BaseBroker):

    def __init__(self):

        self.connected = False
        self.balance = 0
        self.positions = []

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

        return {

            "success": True,

            "broker": "Binance",

            "broker_order_id": "BN-LIVE-000001",

            "order": order

        }

    def cancel_order(self, broker_order_id):

        return {

            "success": True,

            "broker_order_id": broker_order_id

        }

    def modify_order(self, broker_order_id, changes):

        return {

            "success": True,

            "broker_order_id": broker_order_id,

            "changes": changes

        }

    def close_position(self, broker_order_id):

        return {

            "success": True,

            "broker_order_id": broker_order_id

        }