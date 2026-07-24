from datetime import datetime, UTC


class MarketDataManager:

    def __init__(self):
        self.prices = {}

    def update_price(self, symbol, price):

        self.prices[symbol] = {
            "price": price,
            "timestamp": datetime.now(UTC)
        }

    def get_price(self, symbol):

        return self.prices.get(symbol)

    def symbols(self):

        return list(self.prices.keys())

    def print(self):

        print()
        print("=" * 60)
        print("MARKET DATA")
        print("=" * 60)
        print()

        if not self.prices:
            print("No market data.")
            return

        for symbol, data in self.prices.items():

            print(
                f"{symbol:10} "
                f"{data['price']:>10} "
                f"{data['timestamp']}"
            )