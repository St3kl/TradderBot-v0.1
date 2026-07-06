from pprint import pprint

from app.statistics.metrics_engine import MetricsEngine


engine = MetricsEngine()

metrics = engine.build()

pprint(metrics)