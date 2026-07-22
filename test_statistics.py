from pprint import pprint

from Tradderbot_v01.app.analysis.statistics import StatisticsEngine


stats = StatisticsEngine()

pprint(

    stats.summary()

)