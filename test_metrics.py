from pprint import pprint

from app.analytics.metrics import MetricsEngine


metrics = MetricsEngine()

pprint(

    metrics.metrics()

)