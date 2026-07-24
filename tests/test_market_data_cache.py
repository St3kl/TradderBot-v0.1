from app.market.market_data_cache import MarketDataCache

cache = MarketDataCache(max_size=5)

prices = [

    65000,
    65020,
    65050,
    65010,
    65100,
    65200

]

for p in prices:

    cache.update(

        "BTCUSDT",

        p

    )

cache.print()

print()

print(cache.history("BTCUSDT"))

print()

print(cache.latest("BTCUSDT"))

print()

print(cache.size("BTCUSDT"))