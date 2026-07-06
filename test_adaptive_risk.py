from app.risk.adaptive_risk_engine import AdaptiveRiskEngine

engine = AdaptiveRiskEngine()

risk = engine.calculate(100)

print()

print("Adaptive Risk")

print(risk)