from app.testing.base_test import BaseTest


class TestLearning(BaseTest):

    def run(self):

        self.title("LEARNING ENGINE")

        trade = self.trade()

        result = self.learning.learn(trade)

        self.show(result)


TestLearning().run()