from app.strategy.strategy_engine import StrategyEngine
from app.core.registry import engine

session = engine.analyze("BTCUSDT")

session.strategy = "TREND"

StrategyEngine().execute(session)

print()

print(session.strategy_rules)