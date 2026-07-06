# from pprint import pprint

# from app.analytics.equity_curve import EquityCurveEngine


# curve = EquityCurveEngine()

# pprint(

#     curve.build_curve()

# )

from pprint import pprint

from app.statistics.equity_curve import EquityCurve


curve = EquityCurve().build()

pprint(curve)