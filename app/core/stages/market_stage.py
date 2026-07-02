from app.market.indicators import get_market_indicators
from app.market.forex_indicators import get_forex_indicators


class MarketStage:

    def run(self, session):

        symbol = session.symbol

        if symbol.endswith("USDT"):

            session.indicators = get_market_indicators(symbol)

        else:

            forex_symbol = symbol[:3] + "/" + symbol[3:]

            session.indicators = get_forex_indicators(
                forex_symbol
            )

        print("✓ Market loaded")

        return session