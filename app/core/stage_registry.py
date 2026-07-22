from app.core.stages.market_stage import MarketStage
from app.core.stages.trend_stage import TrendStage
from app.core.stages.pattern_stage import PatternStage
from app.core.stages.support_resistance_stage import SupportResistanceStage
from app.core.stages.trade_stage import TradeStage
from app.core.stages.structure_stage import StructureStage
from app.core.stages.smart_money_stage import SmartMoneyStage
from app.core.stages.volume_stage import VolumeStage
from app.core.stages.multi_timeframe_stage import MultiTimeframeStage
from app.core.stages.confluence_stage import ConfluenceStage
from app.core.stages.strategy_stage import StrategyStage
from app.core.stages.validation_stage import ValidationStage
from app.core.stages.checklist_stage import ChecklistStage
from app.core.stages.ai_stage import AIStage
from app.core.stages.report_stage import ReportStage
from app.core.stages.decision_stage import DecisionStage
from app.core.stages.trade_quality_stage import TradeQualityStage


class StageRegistry:

    @staticmethod
    def get_stages():

        return [

    MarketStage(),

    TrendStage(),

    PatternStage(),

    SupportResistanceStage(),

    StructureStage(),

    SmartMoneyStage(),

    VolumeStage(),

    MultiTimeframeStage(),

    ConfluenceStage(),

    StrategyStage(),

    TradeStage(),
    
    ValidationStage(),
    
    DecisionStage(),  # <-- NEW
    
    TradeQualityStage(),

    ChecklistStage(),

    AIStage(),

    ReportStage()

]