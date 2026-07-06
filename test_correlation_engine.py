from app.portfolio.correlation_engine import CorrelationEngine

engine = CorrelationEngine()

symbols = [

    "BTCUSDT",

    "ETHUSDT",

    "EURUSD",

    "XAUUSD"

]

for symbol in symbols:

    print(

        symbol,

        "->",

        engine.group(symbol)

    )