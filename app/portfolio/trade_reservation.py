from datetime import datetime, timedelta


class TradeReservation:

    def __init__(self):

        self.reservations = {}

    def reserve(

        self,

        symbol,

        minutes=2,

        now=None

    ):

        if now is None:

            now = datetime.utcnow()

        expiry = now + timedelta(minutes=minutes)

        self.reservations[symbol] = expiry

    def available(

        self,

        symbol,

        now=None

    ):

        if now is None:

            now = datetime.utcnow()

        expiry = self.reservations.get(symbol)

        if expiry is None:

            return True

        if now >= expiry:

            del self.reservations[symbol]

            return True

        return False

    def release(self, symbol):

        self.reservations.pop(symbol, None)

    def print(self):

        print()

        print("=" * 60)
        print("ACTIVE RESERVATIONS")
        print("=" * 60)
        print()

        if not self.reservations:

            print("None")
            return

        for symbol, expiry in self.reservations.items():

            print(symbol, "->", expiry)