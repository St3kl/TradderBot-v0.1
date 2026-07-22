from app.memory.memory_repository import MemoryRepository


class MemoryEngine:

    def __init__(self):

        self.repo = MemoryRepository()

    def remember(self, session):

        record = {

            "symbol": session.symbol,

            "strategy": session.strategy,

            "direction": session.trade_plan.direction,

            "entry": session.trade_plan.entry,

            "stop_loss": session.trade_plan.stop_loss,

            "take_profit": session.trade_plan.take_profit,

            "risk_reward": session.trade_plan.risk_reward,

            "confidence": session.decision["confidence"],

            "trend": session.structure.trend,

            "phase": session.structure.phase,

            "confluence": session.confluence["score"],

            "volume": session.volume,

            "smart_money": session.smart_money,

            "decision": session.decision["action"]

        }

        self.repo.save(record)