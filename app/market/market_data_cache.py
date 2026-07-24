from collections import deque


class MarketDataCache:

    def __init__(self, max_size=500):

        self.max_size = max_size
        self.cache = {}

    def update(self, symbol, price):

        if symbol not in self.cache:
            self.cache[symbol] = deque(maxlen=self.max_size)

        self.cache[symbol].append(price)

    def history(self, symbol):

        return list(self.cache.get(symbol, []))

    def latest(self, symbol):

        if symbol not in self.cache:
            return None

        if not self.cache[symbol]:
            return None

        return self.cache[symbol][-1]

    def size(self, symbol):

        return len(self.cache.get(symbol, []))

    def symbols(self):

        return list(self.cache.keys())

    def print(self):

        print()
        print("=" * 60)
        print("MARKET DATA CACHE")
        print("=" * 60)
        print()

        for symbol in self.symbols():

            print(
                f"{symbol:10}"
                f" Samples:{self.size(symbol):4}"
                f" Latest:{self.latest(symbol)}"
            )