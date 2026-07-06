from app.learning.statistics import Statistics
from app.learning.performance import Performance


class LearningEngine:

    def __init__(self):

        self.stats = Statistics()
        self.performance = Performance()

    def report(self):

        wins = self.stats.wins()
        losses = self.stats.losses()

        total = wins + losses

        if total:

            win_rate = round((wins / total) * 100, 2)

        else:

            win_rate = 0

        return {

            "total_trades": self.stats.total_trades(),

            "wins": wins,

            "losses": losses,

            "win_rate": win_rate,

            "average_pnl": self.performance.average_pnl(),

            "total_pnl": self.performance.total_pnl()

        }