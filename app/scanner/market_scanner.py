from app.core.registry import engine


class MarketScanner:

    def scan(self, symbol):

        print("=" * 60)

        print(f"Scanning {symbol}")

        session = engine.analyze(symbol)

        return session