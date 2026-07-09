from pprint import pprint

from app.learning.learning_engine import LearningEngine
from app.paper.paper_engine import PaperTradingEngine

from app.testing.factories.trade_factory import TradeFactory
from app.testing.factories.session_factory import SessionFactory
from app.testing.factories.execution_factory import ExecutionFactory

from app.testing.helpers.assertions import Assertions


class BaseTest:
    """
    Base class used by every TradderBot test.
    """

    def __init__(self):

        self.learning = LearningEngine()

        self.paper = PaperTradingEngine()

    # -------------------------
    # Factories
    # -------------------------

    def trade(self, **kwargs):

        return TradeFactory.create(**kwargs)

    def session(self, **kwargs):

        return SessionFactory.create(**kwargs)

    def execution(self, **kwargs):

        return ExecutionFactory.create(**kwargs)

    # -------------------------
    # Assertions
    # -------------------------

    def assert_trade(self, trade):

        Assertions.valid_trade(trade)

    def assert_session(self, session):

        Assertions.valid_session(session)

    def assert_execution(self, execution):

        Assertions.valid_execution(execution)

    # -------------------------
    # Output
    # -------------------------

    def title(self, text):

        print()

        print("=" * 20)

        print(text)

        print("=" * 20)

    def show(self, obj):

        pprint(obj)

    def success(self):

        print("\n✓ TEST PASSED\n")