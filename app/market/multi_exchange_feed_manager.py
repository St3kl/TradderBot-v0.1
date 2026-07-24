class MultiExchangeFeedManager:

    def __init__(self):

        self.feeds = {}

    def register(self, name, websocket_manager):

        self.feeds[name] = websocket_manager

    def connect_all(self):

        for feed in self.feeds.values():

            if feed.endpoint:

                feed.connect(feed.endpoint)

    def disconnect_all(self):

        for feed in self.feeds.values():

            feed.disconnect()

    def status(self):

        report = {}

        for name, feed in self.feeds.items():

            report[name] = feed.status()

        return report

    def print(self):

        print()

        print("=" * 60)
        print("MULTI-EXCHANGE FEED MANAGER")
        print("=" * 60)
        print()

        if not self.feeds:
            print("No feeds registered.")
            return

        for name, feed in self.feeds.items():

            print(

                f"{name:12}",

                "CONNECTED" if feed.is_connected() else "DISCONNECTED"

            )