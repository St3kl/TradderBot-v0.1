from app.quality.trade_quality import TradeQuality


class Session:

    pass


session = Session()

session.confluence = {"score": 80}

session.validation = {"score": 90}

session.decision = {"confidence": 85}

session.market_health = {"score": 100}

session.volatility = {"score": 50}

session.correlation = {"score": 75}


quality = TradeQuality()

print(quality.calculate(session))