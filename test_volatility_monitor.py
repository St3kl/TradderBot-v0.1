from app.intelligence.volatility_monitor import VolatilityMonitor


class Dummy:
    pass


session = Dummy()

session.indicators = {
    "price": 64000,
    "atr": 360,
}

engine = VolatilityMonitor()

print(engine.evaluate(session))