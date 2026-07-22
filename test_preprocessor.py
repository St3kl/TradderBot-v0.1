from app.market.data.manager import MarketDataManager
from app.market.preprocessing.dataset_preprocessor import DatasetPreprocessor

manager = MarketDataManager()

df = manager.get_dataset(
    "BTCUSDT",
    "1H",
    limit=300
)

processor = DatasetPreprocessor()

df = processor.process(df)

print(df.columns)

print(
    df[
        [
            "close",
            "ema50",
            "ema200",
            "rsi",
            "atr",
            "adx"
        ]
    ].tail()
)