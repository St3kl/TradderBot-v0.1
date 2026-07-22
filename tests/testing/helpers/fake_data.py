from random import uniform


class FakeData:
    """
    Generates reusable fake market values.
    """

    @staticmethod
    def btc_price():

        return round(uniform(60000, 65000), 2)

    @staticmethod
    def confidence():

        return round(uniform(55, 95), 2)

    @staticmethod
    def risk_amount():

        return 100

    @staticmethod
    def rr():

        return 2.0

    @staticmethod
    def bullish():

        return True

    @staticmethod
    def bearish():

        return False