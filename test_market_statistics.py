from pprint import pprint

from app.learning.market_statistics import MarketStatistics

stats = MarketStatistics()

pprint(stats.summary())