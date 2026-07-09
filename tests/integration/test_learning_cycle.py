from tests.base import TestCase


class TestLearningCycle(TestCase):

    def run(self):

        self.title("LEARNING CYCLE")

        session = self.session()

        execution = self.execution()

        trade = self.paper.open_trade(

            session,

            execution

        )

        recommendation = self.learning.learn(

            trade

        )

        self.show(recommendation)

        self.success()


TestLearningCycle().run()