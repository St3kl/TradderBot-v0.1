from app.market.trend import TrendEngine
from app.market.volume import VolumeEngine


class MarketEngine:

    def __init__(self):

        self.trend = TrendEngine()

        self.volume = VolumeEngine()

        # Future

        self.regime = None

        self.structure = None

        self.patterns = None

        self.smart_money = None

    # ------------------------------------

    def analyze(self, session):

        session.market["trend"] = self.trend.analyze(session)

        session.market["volume"] = self.volume.analyze(session)

        return session