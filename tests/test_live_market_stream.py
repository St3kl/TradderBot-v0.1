from app.market.market_data_manager import MarketDataManager
from app.market.market_data_cache import MarketDataCache
from app.market.tick_aggregator import TickAggregator
from app.market.candle_builder import CandleBuilder
from app.market.live_market_stream import LiveMarketStream

manager = MarketDataManager()
cache = MarketDataCache(max_size=10)
aggregator = TickAggregator()
builder = CandleBuilder()

stream = LiveMarketStream(

    manager,

    cache,

    aggregator,

    builder

)

prices = [

    65000,

    65020,

    65050,

    64990,

    65100

]

for p in prices:

    stream.on_tick(

        "BTCUSDT",

        p,

        volume=1

    )

print()

print("=" * 60)

print("LIVE MARKET STREAM")

print("=" * 60)

print()

print(stream.status())

print()

builder.print()