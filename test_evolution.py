from app.ai.memory.memory_engine import MemoryEngine

memory = MemoryEngine()

report = memory.evolution("BTCUSDT")

print(report)