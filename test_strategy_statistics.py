from pprint import pprint

from app.learning.strategy_statistics import StrategyStatistics

stats = StrategyStatistics()

pprint(stats.summary())