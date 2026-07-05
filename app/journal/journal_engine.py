from copy import deepcopy
from datetime import datetime


class JournalEngine:

    def build_entry(self, session):

        return {

            "symbol": session.symbol,

            "trend": deepcopy(session.trend),

            "market": deepcopy(session.indicators),

            "structure": deepcopy(session.structure),

            "smart_money": deepcopy(session.smart_money),

            "trade": deepcopy(session.trade),

            "decision": deepcopy(session.decision),

            "validation": deepcopy(session.validation),

            "reasoning": deepcopy(session.ai_reasoning),

            "timestamp": datetime.utcnow().isoformat(),

        }