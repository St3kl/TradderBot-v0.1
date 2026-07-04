from app.core.registry import engine
from app.execution.entry_engine import EntryEngine

session = engine.analyze("BTCUSDT")

entry = EntryEngine()

print(

    entry.evaluate(session)

)