from pprint import pprint

from app.analytics.statistics import StatisticsEngine


stats = StatisticsEngine()

pprint(

    stats.summary()

)