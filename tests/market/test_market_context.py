from tests.base import TestCase


class TestExample(TestCase):

    def run(self):

        self.title("EXAMPLE TEST")

        #
        # Arrange
        #

        session = self.session()

        execution = self.execution()

        #
        # Act
        #

        trade = self.paper.open_trade(

            session,

            execution

        )

        #
        # Assert
        #

        self.assert_trade(trade)

        self.show(trade)

        self.success()


TestExample().run()