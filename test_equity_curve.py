from pprint import pprint

from app.analytics.equity_curve import EquityCurveEngine


curve = EquityCurveEngine()

pprint(

    curve.build_curve()

)