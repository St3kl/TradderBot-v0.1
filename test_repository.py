from app.market.data.downloader import BinanceDownloader
from app.market.data.repository import MarketDataRepository

repo = MarketDataRepository()
downloader = BinanceDownloader()

df = downloader.download(
    "BTCUSDT",
    "1h",
    100
)

filename = repo.save(
    "BTCUSDT",
    "1h",
    df
)

print(filename)

loaded = repo.load(
    "BTCUSDT",
    "1h"
)

print(loaded.head())

print(len(loaded))