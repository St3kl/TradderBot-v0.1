from pprint import pprint

from Tradderbot_v01.app.analysis.metrics import MetricsEngine


metrics = MetricsEngine()

pprint(

    metrics.metrics()

)