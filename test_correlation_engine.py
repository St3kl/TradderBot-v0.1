from app.intelligence.correlation_engine import CorrelationEngine


class Dummy:
    pass


session = Dummy()

session.multi_timeframe = {

    "15m": "Bullish",

    "1h": "Bullish",

    "4h": "Bullish",

    "1d": "Bearish",

}

engine = CorrelationEngine()

print(engine.evaluate(session))