from app.analytics.streak_analyzer import StreakAnalyzer

trades = [

    {"result":"WIN"},
    {"result":"WIN"},
    {"result":"LOSS"},
    {"result":"LOSS"},
    {"result":"LOSS"},
    {"result":"WIN"},
    {"result":"WIN"},
    {"result":"WIN"},
    {"result":"WIN"},
    {"result":"LOSS"}

]

engine = StreakAnalyzer()

report = engine.analyze(trades)

engine.print(report)