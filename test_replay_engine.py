from app.replay.replay_engine import ReplayEngine

class Session:
    pass

s = Session()

s.symbol = "BTCUSDT"

s.trend = {"direction":"Bullish"}

s.structure = {}

s.smart_money = {}

s.confluence = {}

s.decision = {"action":"LONG"}

s.trade = {"entry":100}

ReplayEngine().save(s)

print("Replay saved.")