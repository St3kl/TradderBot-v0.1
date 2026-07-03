from app.core.registry import engine
from app.ai.memory.memory_engine import MemoryEngine

session = engine.analyze("BTCUSDT")

memory = MemoryEngine()

memory.save(session)

print(memory.load("BTCUSDT"))