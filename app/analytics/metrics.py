from app.analytics.statistics import StatisticsEngine


class MetricsEngine:

    def __init__(self):

        self.stats = StatisticsEngine()

    def win_rate(self):

        closed = self.stats.closed_trades()

        if closed == 0:

            return 0.0

        return round(

            self.stats.wins() / closed * 100,

            2

        )

    def loss_rate(self):

        closed = self.stats.closed_trades()

        if closed == 0:

            return 0.0

        return round(

            self.stats.losses() / closed * 100,

            2

        )

    def metrics(self):

        return {

            "win_rate": self.win_rate(),

            "loss_rate": self.loss_rate()

        }