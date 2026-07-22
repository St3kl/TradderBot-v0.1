from app.market.data.manager import MarketDataManager

manager = MarketDataManager()

df = manager.get_dataset(

    "BTCUSDT",

    "1H",

    limit=250

)

print(df.head())

print(len(df))