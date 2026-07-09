from app.market.indicators import get_market_indicators


class LiveDataProvider:

    def get_indicators(self, symbol):

        return get_market_indicators(symbol)