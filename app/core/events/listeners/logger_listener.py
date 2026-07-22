class LoggerListener:

    def handle(self, trade):

        print(

            f"Trade Closed -> {trade['symbol']}"

        )