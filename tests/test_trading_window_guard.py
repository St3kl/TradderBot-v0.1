from app.risk.trading_window_guard import TradingWindowGuard

class Session:
    pass

guard = TradingWindowGuard()

session = Session()

session.market_health = {"score": 80}

session.volatility = {"level": "NORMAL"}

session.correlation = {"score": 75}

print(guard.evaluate(session))

session.market_health = {"score": 25}

session.volatility = {"level": "EXTREME"}

session.correlation = {"score": 20}

print(guard.evaluate(session))