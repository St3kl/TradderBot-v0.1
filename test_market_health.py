from app.intelligence.market_health import MarketHealth


class Dummy:
    pass


session = Dummy()

session.trend = {

    "confidence": 70

}

session.volume = {

    "score": 40

}

session.confluence = {

    "score": 80

}

session.validation = {

    "score": 90

}

session.structure = Dummy()

session.structure.trend = "Trending"

session.market_regime = {

    "regime": "TRENDING"

}

engine = MarketHealth()

print(engine.evaluate(session))