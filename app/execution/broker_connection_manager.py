class BrokerConnectionManager:

    def __init__(self, broker):

        self.broker = broker

    def connect(self):

        if self.broker.is_connected():

            return True

        return self.broker.connect()

    def disconnect(self):

        if self.broker.is_connected():

            self.broker.disconnect()

    def ensure_connection(self):

        if not self.broker.is_connected():

            return self.connect()

        return True

    def status(self):

        return {

            "connected": self.broker.is_connected()

        }

    def print(self):

        print()

        print("=" * 60)
        print("BROKER CONNECTION")
        print("=" * 60)
        print()

        print("Connected :", self.broker.is_connected())