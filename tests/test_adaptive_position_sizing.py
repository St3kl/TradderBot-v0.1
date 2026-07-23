from app.portfolio.adaptive_position_sizing import AdaptivePositionSizing

engine = AdaptivePositionSizing()

balance = 10000

for mode in [

    {"mode":"AGGRESSIVE"},

    {"mode":"NORMAL"},

    {"mode":"DEFENSIVE"},

    {"mode":"SURVIVAL"}

]:

    report = engine.calculate(

        balance,

        mode

    )

    engine.print(report)