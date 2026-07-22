from types import SimpleNamespace

from app.decision.decision_engine import DecisionEngine

session = SimpleNamespace()

session.confluence = {"confidence": 80}

session.validation = {
    "valid": True,
    "confidence": 90
}

session.trend = {
    "bullish": True,
    "confidence": 85
}

session.ai = {
    "confidence": 80
}

engine = DecisionEngine()

session = engine.evaluate(session)

print(session.decision)