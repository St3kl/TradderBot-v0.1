from app.market.data.downloader import BinanceDownloader

downloader = BinanceDownloader()

df = downloader.download(
    "BTCUSDT",
    "1h"
)

print(df.head())
print()
print(df.tail())
print()
print(len(df))