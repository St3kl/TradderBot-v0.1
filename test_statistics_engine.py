from pprint import pprint

from app.statistics.statistics_engine import StatisticsEngine


engine = StatisticsEngine()

stats = engine.build()

pprint(stats)