from app.market_structure.trend import detect_trend

swing_highs = [

    (5,100),

    (12,108),

    (18,115)

]

swing_lows = [

    (3,90),

    (10,95),

    (16,101)

]

trend = detect_trend(
    swing_highs,
    swing_lows
)

print(trend)