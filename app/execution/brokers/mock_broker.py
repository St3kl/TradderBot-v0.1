from app.execution.brokers.base_broker import BaseBroker


class MockBroker(BaseBroker):

    def __init__(self):

        self.connected = False

    def connect(self):

        self.connected = True

        return True

    def disconnect(self):

        self.connected = False

    def is_connected(self):

        return self.connected

    def place_order(self, order):

        return {

            "success": True,

            "broker_order_id": "MOCK-000001"

        }

    def modify_order(self, order):

        return True

    def cancel_order(self, broker_order_id):

        return True

    def get_order(self, broker_order_id):

        return {

            "status": "FILLED"

        }

    def get_positions(self):

        return []

    def get_balance(self):

        return 100000