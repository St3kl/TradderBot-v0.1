from app.backtesting.replay_engine import ReplayEngine
from app.backtesting.candle_player import CandlePlayer

from app.backtesting.pipeline_runner import PipelineRunner

from app.backtesting.trade_simulator import TradeSimulator
from app.backtesting.performance_analyzer import PerformanceAnalyzer
from app.backtesting.report_generator import ReportGenerator
from app.backtesting.equity_curve import EquityCurve

from app.market.data.manager import MarketDataManager
from app.history.decision_history import DecisionHistory
from app.memory.memory_engine import MemoryEngine
from app.analytics.analytics_engine import AnalyticsEngine
from app.adaptive.adaptive_engine import AdaptiveEngine
from app.ai_coach.ai_coach import AICoach
from app.audit.audit_engine import AuditEngine
from app.history.trade_journal import TradeJournal
from app.analytics.performance_dashboard import PerformanceDashboard
from app.backtesting.opportunity_scanner import OpportunityScanner

class BacktestEngine:

    def __init__(
        self,
        trading_engine,
        execution,
        learning,
        trade_manager,
        portfolio,
        paper,
    ):

        self.replay = ReplayEngine()
        self.market_data = MarketDataManager()
        self.runner = PipelineRunner(trading_engine)
        

        self.history = DecisionHistory()
        self.execution = execution
        self.learning = learning
        self.trade_manager = trade_manager
        self.portfolio = portfolio
        self.paper = paper

        self.simulator = TradeSimulator()

        self.performance = PerformanceAnalyzer()
        self.report = ReportGenerator()

        self.equity_curve = EquityCurve()


        self.adaptive = AdaptiveEngine()

        self.analytics = AnalyticsEngine()

        self.memory = MemoryEngine()

        self.coach = AICoach()
        
        self.audit = AuditEngine()
        
        self.trade_journal = TradeJournal()
        
        self.dashboard = PerformanceDashboard()
        
        self.scanner = OpportunityScanner()

    def run(
        self,
        symbol,
        timeframe,
        start,
        end,
    ):
        
        
        analytics = self.analytics.analyze(

            self.trade_manager.get_closed()

        )

        print()

        print("="*60)

        print("ANALYTICS")

        print("="*60)

        print(analytics)

        print()
        print("=" * 50)
        print("BACKTEST STARTED")
        print("=" * 50)
        print()

        df = self.market_data.get_dataset(
            symbol=symbol,
            timeframe=timeframe,
            limit=1000,
            refresh=False
        )
        print(df.columns)
        candles = df.to_dict("records")

        self.replay.load(
            candles,
            symbol
        )

        player = CandlePlayer(self.replay)

        for context in player.play():

            print(f"Replay -> {context.candle['time']}")

            session = self.runner.analyze(
                context,
                balance=self.portfolio.balance,
            )
            self.scanner.scan(session)
            self.history.save(session)
            self.memory.remember(session)
            

            # ---------------------------------------
            # Update Existing Trades
            # ---------------------------------------

            for trade in self.trade_manager.get_open().copy():

                result = self.simulator.update(
                trade,
                context.candle,
                )

                if result["closed"]:

                    closed_trade = self.paper.close_trade(
                        trade,
                        result["exit_price"],
                        result["result"],
                    )

                    self.trade_manager.close(
                        closed_trade
                    )

                    # Portfolio update
                    self.portfolio.apply_trade(
                        closed_trade
                    )
                    
                    self.trade_journal.save(closed_trade)

                    # Equity curve
                    self.equity_curve.add(
                        self.portfolio.balance
                    )

                    # Learning is now handled by LearningSubscriber

            # ---------------------------------------
            # Evaluate Execution
            # ---------------------------------------

            execution = self.execution.evaluate(

                session=session,

                balance=self.portfolio.balance,

                risk_percent=1,

                open_positions=self.trade_manager.get_open(),

            )

            # ---------------------------------------
            # Open New Trade
            # ---------------------------------------

            trade = self.paper.open_trade(
                session,
                execution,
            )

            if trade:

                self.trade_manager.add(
                    trade
                )

                print("Trade Executed")

            else:

                print("No Trade")

        print()
        print("=" * 50)
        print("Replay Finished")
        print("=" * 50)
        
        # Save the last analyzed session
        last_session = session
        
        portfolio = self.portfolio.summary()

        performance = self.performance.analyze(
        self.trade_manager.get_closed()
        )
        
        dashboard = self.dashboard.summarize(
            self.trade_manager.get_closed()
        )

        learning = self.learning.statistics()
        
        
        coach = self.coach.review(

            self.trade_manager.get_closed(),

            learning

        )

        print()

        print("=" * 60)

        print("AI COACH")

        print("=" * 60)
        
        print()

        print("=" * 60)
        print("PERFORMANCE DASHBOARD")
        print("=" * 60)

        for key, value in dashboard.items():
            print(f"{key:<20}: {value}")

        print()
        
        

        for section, messages in coach.items():

            print(f"\n{section.upper()}")

            for message in messages:

                print("-", message)
        
        
        adaptive = self.adaptive.evaluate(

        learning["strategy"]

        )
        
        print()
        print("=" * 60)
        print("OPPORTUNITY SCANNER")
        print("=" * 60)

        summary = self.scanner.summary()

        print(f"Total Opportunities : {summary['total']}")
        print(f"Valid Trades        : {summary['valid']}")
        print(f"Rejected Trades     : {summary['rejected']}")

        print()
        print("Strategy Frequency")

        for strategy, total in self.scanner.by_strategy().items():
            print(f"{strategy:<15}{total}")

        print()
        print("Top Rejection Reasons")

        for reason, total in self.scanner.top_rejections().items():
            print(f"{reason:<30}{total}")

        print()

        print("=" * 60)

        print("STRATEGY RANKING")

        print("=" * 60)

        for row in adaptive["ranking"]:

            print(

                row["strategy"],

                row["score"]

            )

        report = self.report.generate(

            portfolio=portfolio,

            performance=performance,

            strategy_stats=learning["strategy"],

            market_stats=learning["market"],

            learning=learning["ai"]

        )
        
        audit = self.audit.analyze(last_session)

        print()
        print("=" * 60)
        print("SIGNAL AUDIT")
        print("=" * 60)

        for item, passed in audit["checklist"].items():

            status = "PASS" if passed else "FAIL"

        print(f"{item:<25} {status}")

        print()

        print(
            f"Score: {audit['breakdown']['score']}%"
        )

        print()

        print("Rejected because:")

        for reason in audit["rejected"]:

            print("-", reason)
        

        self.report.print(report)

        return {
            "report": report,
            "session": last_session
        }
        
        