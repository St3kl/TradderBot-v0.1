from app.market.indicator_cache import IndicatorCache
from app.market.data.manager import MarketDataManager

manager = MarketDataManager()

df = manager.get_dataset(
    "BTCUSDT",
    "1H",
    limit=20
)

cache = IndicatorCache()

cache.load(df)

print(cache.size())

print(cache.candle(0))