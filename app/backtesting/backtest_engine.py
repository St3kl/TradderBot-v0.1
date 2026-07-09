from app.backtesting.replay_engine import ReplayEngine
from app.backtesting.candle_player import CandlePlayer
from app.backtesting.datasets.loader import DatasetLoader
from app.backtesting.pipeline_runner import PipelineRunner

from app.execution.execution_manager import ExecutionManager
from app.paper.paper_engine import PaperTradingEngine

from app.backtesting.trade_simulator import TradeSimulator

from app.learning.learning_engine import LearningEngine
from app.backtesting.trade_manager import TradeManager

from app.backtesting.portfolio_manager import PortfolioManager




class BacktestEngine:

    def __init__(self):

        self.replay = ReplayEngine()
        self.loader = DatasetLoader()
        self.runner = PipelineRunner()

        self.execution = ExecutionManager()
        self.paper = PaperTradingEngine()
        
        self.simulator = TradeSimulator()

        self.learning = LearningEngine()

        self.trade_manager = TradeManager()
        self.portfolio = PortfolioManager(initial_balance=10000)

    def run(
    self,
    symbol,
    timeframe,
    start,
    end
):

        print()
        print("=" * 50)
        print("BACKTEST STARTED")
        print("=" * 50)
        print()

        candles = self.loader.load(
            "data/BTCUSDT/BTCUSDT_1H.csv"
        )

        self.replay.load(candles)

        player = CandlePlayer(self.replay)

        balance = 10000

        for candle in player.play():

            print()
            print(f"Replay -> {candle['time']}")

            session = self.runner.analyze(symbol)

            execution = self.execution.evaluate(
                session=session,
                balance=balance,
                risk_percent=1,
                open_positions=[]
            )

            trade = self.paper.open_trade(
                session,
                execution
            )

            if trade:
                print("Trade Executed")
            else:
                print("No Trade")

        print()
        print("Replay Finished")