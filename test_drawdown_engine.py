from pprint import pprint

from app.statistics.drawdown_engine import DrawdownEngine


engine = DrawdownEngine()

stats = engine.build()

pprint(stats)