from pprint import pprint

from app.orchestrator.ai_pipeline import AIPipeline

from app.market.market_engine import MarketEngine
from app.execution.execution_manager import ExecutionManager
from app.paper.paper_engine import PaperTradingEngine
from app.learning.learning_engine import LearningEngine
from app.backtesting.portfolio_manager import PortfolioManager

pipeline = AIPipeline(

    MarketEngine(),

    ExecutionManager(),

    PaperTradingEngine(),

    LearningEngine(),

    PortfolioManager(initial_balance=10000)

)

ctx = pipeline.process(

    "BTCUSDT"

)

print()

print("=" * 50)

print("AI PIPELINE")

print("=" * 50)

print()

pprint(ctx.decision)

print()

print("✓ TEST PASSED")