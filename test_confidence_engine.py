from types import SimpleNamespace

from app.decision.confidence_engine import ConfidenceEngine

session = SimpleNamespace()

session.confluence = {"confidence":40}
session.validation = {"confidence":90}
session.trend = {"confidence":70}
session.ai = {"confidence":80}

engine = ConfidenceEngine()

print(engine.calculate(session))