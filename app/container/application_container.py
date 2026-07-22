from app.execution.execution_manager import ExecutionManager
from app.learning.learning_engine import LearningEngine

from app.backtesting.trade_manager import TradeManager
from app.backtesting.portfolio_manager import PortfolioManager
from app.backtesting.backtest_engine import BacktestEngine

from app.paper.paper_engine import PaperTradingEngine

from app.core.engine import TradingEngine
from app.core.events.event_bus import EventBus

from app.config.config_loader import ConfigLoader

from app.events.subscribers.learning_subscriber import (
    LearningSubscriber
)
from app.journal.trade_journal import TradeJournal
from app.events.event_types import TradeExecuted
from app.events.subscribers.portfolio_subscriber import (
    PortfolioSubscriber
)
from app.events.subscribers.journal_subscriber import (
    JournalSubscriber
)

from app.events.subscribers.notification_subscriber import (
    NotificationSubscriber
)

from app.learning.adaptive_config import AdaptiveConfig



class ApplicationContainer:
    """
    Dependency Injection Container

    Services are created lazily and cached.
    """

    def __init__(self):

        self._instances = {}

        self.config = ConfigLoader()
        
        

    # ------------------------------------
    # Configuration
    # ------------------------------------

    def settings(self):

        return self.config

    # ------------------------------------
    # Event Bus
    # ------------------------------------

    def event_bus(self):

        if "event_bus" not in self._instances:

            self._instances["event_bus"] = EventBus()

        return self._instances["event_bus"]

    # ------------------------------------
    # Trading Engine
    # ------------------------------------

    def trading_engine(self):

        if "trading_engine" not in self._instances:

            self._instances["trading_engine"] = TradingEngine(

            adaptive_config=self.adaptive_config()

        )

        return self._instances["trading_engine"]

    # ------------------------------------
    # Trade Manager
    # ------------------------------------

    def trade_manager(self):

        if "trade_manager" not in self._instances:

            self._instances["trade_manager"] = TradeManager()

        return self._instances["trade_manager"]

    # ------------------------------------
    # Portfolio
    # ------------------------------------

    def portfolio(self):

        if "portfolio" not in self._instances:

            self._instances["portfolio"] = PortfolioManager(

                initial_balance=self.config.get(
                    "portfolio",
                    "initial_balance"
                )

            )

        return self._instances["portfolio"]

    # ------------------------------------
    # Execution
    # ------------------------------------

    def execution(self):

        if "execution" not in self._instances:

            self._instances["execution"] = ExecutionManager(

                event_bus=self.event_bus()

            )

        return self._instances["execution"]

    # ------------------------------------
    # Learning
    # ------------------------------------

    def learning(self):

        if "learning" not in self._instances:

            self._instances["learning"] = LearningEngine(

            adaptive_config=self.adaptive_config()

            )

        return self._instances["learning"]

    # ------------------------------------
    # Paper Trading
    # ------------------------------------

    def paper(self):

        if "paper" not in self._instances:

            self._instances["paper"] = PaperTradingEngine()

        return self._instances["paper"]

    # ------------------------------------
    # Backtesting
    # ------------------------------------

    def backtest(self):

        if "backtest" not in self._instances:

            self._instances["backtest"] = BacktestEngine(

                trading_engine=self.trading_engine(),

                execution=self.execution(),

                learning=self.learning(),

                trade_manager=self.trade_manager(),

                portfolio=self.portfolio(),

                paper=self.paper()

            )

        return self._instances["backtest"]

        # ------------------------------------
    # Subscribers
    # ------------------------------------

    def register_subscribers(self):

        bus = self.event_bus()

        learning_subscriber = LearningSubscriber(
            self.learning()
        )

        bus.subscribe(
            TradeExecuted,
            learning_subscriber.on_trade_executed
        )

        portfolio_subscriber = PortfolioSubscriber(
            self.portfolio()
        )

        bus.subscribe(
            TradeExecuted,
            portfolio_subscriber.on_trade_executed
        )

        journal_subscriber = JournalSubscriber(
            self.journal()
        )

        bus.subscribe(
            TradeExecuted,
            journal_subscriber.on_trade_executed
        )
        
        notification = NotificationSubscriber()

        bus.subscribe(
            TradeExecuted,
            notification.on_trade_executed
        )

    # ------------------------------------
    # Journal
    # ------------------------------------

    def journal(self):

        if "journal" not in self._instances:

            self._instances["journal"] = TradeJournal()

        return self._instances["journal"]
    
    
    def adaptive_config(self):

        if "adaptive_config" not in self._instances:

            self._instances["adaptive_config"] = AdaptiveConfig()

        return self._instances["adaptive_config"]
    
    