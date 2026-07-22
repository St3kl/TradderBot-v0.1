from app.analytics.expectancy_analyzer import ExpectancyAnalyzer

trades = [

    {"profit":200},

    {"profit":150},

    {"profit":-100},

    {"profit":-50},

    {"profit":300}

]

engine = ExpectancyAnalyzer()

result = engine.analyze(trades)

engine.print(result)