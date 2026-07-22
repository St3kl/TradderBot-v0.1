from app.backtesting.opportunity_scanner import OpportunityScanner

scanner = OpportunityScanner()

class Dummy:
    pass

s = Dummy()

s.symbol = "BTCUSDT"

s.strategy = "TREND"

s.replay = Dummy()

s.replay.candle = {"time": "today"}

s.decision = {

    "action": "LONG",

    "confidence": 85,

    "reason": ""

}

scanner.scan(s)

print(scanner.summary())

print(scanner.by_strategy())