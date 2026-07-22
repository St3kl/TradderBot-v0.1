from app.ai.memory.memory_engine import MemoryEngine


class MemoryStage:

    def __init__(self):

        self.memory = MemoryEngine()

    def process(self, trade):

        self.memory.store(trade)