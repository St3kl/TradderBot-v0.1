from app.core.pipeline import TradingPipeline
from app.core.session import TradingSession

from app.core.stages.market_stage import MarketStage
from app.core.stages.pattern_stage import PatternStage
from app.core.stages.structure_stage import StructureStage
from app.core.stages.smart_money_stage import SmartMoneyStage
from app.core.stages.confluence_stage import ConfluenceStage
from app.core.stages.decision_stage import DecisionStage
from app.core.stages.validation_stage import ValidationStage
from app.core.stages.ai_stage import AIStage
from app.core.stages.report_stage import ReportStage

from app.core.stages.trend_stage import TrendStage

class TradingEngine:

    def __init__(self):

        self.pipeline = TradingPipeline()

        self.pipeline.add_step(MarketStage())
        self.pipeline.add_step(PatternStage())
        self.pipeline.add_step(StructureStage())
        self.pipeline.add_step(SmartMoneyStage())
        self.pipeline.add_step(ConfluenceStage())
        self.pipeline.add_step(DecisionStage())
        self.pipeline.add_step(ValidationStage())
        self.pipeline.add_step(AIStage())
        self.pipeline.add_step(ReportStage())
        self.pipeline.add_step(TrendStage())

    def analyze(self, symbol):

        session = TradingSession()

        session.symbol = symbol.upper()

        return self.pipeline.run(session)