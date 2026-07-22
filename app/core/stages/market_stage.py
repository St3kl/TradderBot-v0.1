from app.market.indicators import get_market_indicators
from app.market.forex_indicators import get_forex_indicators
from app.market.regime_engine import RegimeEngine
from app.strategy.strategy_selector import StrategySelector
# from app.market.replay_data_provider import ReplayDataProvider


# class MarketStage:

#     def run(self, session):

#         symbol = session.symbol

# # ---------------------------------
# # Backtesting
# # ---------------------------------

#         if getattr(session, "replay_candles", None):

#             session.indicators = ReplayDataProvider.get(
#             session.replay_candles
#         )

# # ---------------------------------
# # Live Market
# # ---------------------------------

#         elif symbol.endswith("USDT"):

#             session.indicators = get_market_indicators(
#             symbol
#         )

#         else:

#             forex_symbol = symbol[:3] + "/" + symbol[3:]

#             session.indicators = get_forex_indicators(
#             forex_symbol
#         )

#         # ---------------------------------
#         # Detect Market Regime
#         # ---------------------------------

#         regime = RegimeEngine()

#         session.market_regime = regime.classify(
#             session.indicators
#         )

#         # ---------------------------------
#         # Select Strategy
#         # ---------------------------------

#         selector = StrategySelector()

#         session.strategy = selector.select(
#             session.market_regime
            
#         )

#         print("Market Regime:", session.market_regime)
#         print("Selected Strategy:", session.strategy)
#         print("✓ Market loaded")

#         return session


class MarketStage:

    def run(self, session):

        print("Running Market Stage")

        candle = session.replay.candle

        session.market = candle

        session.indicators = {

            "price": candle["close"],

            "ema50": candle["ema50"],

            "ema200": candle["ema200"],

            "rsi": candle["rsi"],

            "atr": candle["atr"],

            "adx": candle["adx"],

            "open": candle["open"],

            "high": candle["high"],

            "low": candle["low"],

            "volume": candle["volume"]

        }

        return session