from pprint import pprint

from app.backtesting.equity_curve import EquityCurve

curve = EquityCurve()

curve.add(10000)
curve.add(10150)
curve.add(10050)
curve.add(10400)
curve.add(10320)

pprint(curve.get())