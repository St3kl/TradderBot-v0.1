import time

from app.scanner.market_scanner import MarketScanner


class Scheduler:

    def __init__(self):

        self.scanner = MarketScanner()

    def run(self, symbol):

        while True:

            session = self.scanner.scan(symbol)

            print(session.decision)

            print()

            time.sleep(60)