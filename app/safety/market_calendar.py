from datetime import datetime, UTC


class MarketCalendar:

    def __init__(self):

        self.weekend_closed = {

            "FOREX": True,

            "STOCKS": True,

            "CRYPTO": False

        }

    def is_market_open(self, market):

        market = market.upper()

        weekday = datetime.now(UTC).weekday()

        if market == "CRYPTO":
            return True

        if weekday >= 5:      # Saturday=5 Sunday=6
            return False

        return True

    def print(self, market):

        print()

        print("=" * 60)
        print("MARKET CALENDAR")
        print("=" * 60)
        print()

        print("Market :", market.upper())
        print("Open   :", self.is_market_open(market))