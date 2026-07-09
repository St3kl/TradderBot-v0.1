from app.learning.learning_engine import LearningEngine

engine = LearningEngine()

trade = {

    "symbol": "BTCUSDT",

    "strategy": "Trend Following",

    "result": "WIN",

    "market_regime": {

        "regime": "TRENDING",

        "volatility": "HIGH"

    },

    "confidence": 82

}

print(engine.learn(trade))