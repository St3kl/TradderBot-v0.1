from app.analytics.signal_quality import SignalQuality

trades = [

    {"confidence": 82, "result": "WIN"},
    {"confidence": 87, "result": "LOSS"},
    {"confidence": 64, "result": "WIN"},
    {"confidence": 66, "result": "WIN"},
]

quality = SignalQuality()

print(quality.analyze(trades))