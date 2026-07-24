from datetime import datetime, UTC


class WebSocketManager:

    def __init__(self):

        self.connected = False
        self.endpoint = None
        self.connected_at = None

    def connect(self, endpoint):

        self.endpoint = endpoint
        self.connected = True
        self.connected_at = datetime.now(UTC)

        return True

    def disconnect(self):

        self.connected = False

    def is_connected(self):

        return self.connected

    def status(self):

        return {

            "connected": self.connected,

            "endpoint": self.endpoint,

            "connected_at": self.connected_at

        }

    def print(self):

        print()

        print("=" * 60)
        print("WEBSOCKET MANAGER")
        print("=" * 60)
        print()

        print("Connected :", self.connected)
        print("Endpoint  :", self.endpoint)
        print("Since     :", self.connected_at)