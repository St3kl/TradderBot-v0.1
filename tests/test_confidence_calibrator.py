from app.analytics.confidence_calibrator import ConfidenceCalibrator

trades = [

    {"confidence":92,"result":"WIN"},
    {"confidence":90,"result":"LOSS"},
    {"confidence":91,"result":"WIN"},

    {"confidence":75,"result":"WIN"},
    {"confidence":78,"result":"LOSS"},
    {"confidence":73,"result":"LOSS"},

    {"confidence":65,"result":"WIN"},
    {"confidence":67,"result":"WIN"}

]

engine = ConfidenceCalibrator()

report = engine.calibrate(trades)

engine.print(report)