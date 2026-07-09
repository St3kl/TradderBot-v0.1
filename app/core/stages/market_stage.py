from app.market.indicators import get_market_indicators
from app.market.forex_indicators import get_forex_indicators
from app.market.regime_engine import RegimeEngine
from app.strategy.strategy_selector import StrategySelector


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

        # ---------------------------------
        # Detect Market Regime
        # ---------------------------------

        regime = RegimeEngine()

        session.market_regime = regime.classify(
            session.indicators
        )

        # ---------------------------------
        # Select Strategy
        # ---------------------------------

        selector = StrategySelector()

        session.strategy = selector.select(
            session.market_regime
            
        )

        print("Market Regime:", session.market_regime)
        print("Selected Strategy:", session.strategy)
        print("✓ Market loaded")

        return session