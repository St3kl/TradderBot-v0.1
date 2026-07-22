from types import SimpleNamespace

from app.ranking.trade_ranking import TradeRankingEngine

engine = TradeRankingEngine()

sessions = []

for score in [90, 70, 55]:

    s = SimpleNamespace()

    s.symbol = f"PAIR_{score}"

    s.trade_quality = {"score": score}
    s.confluence = {"confidence": score}
    s.validation = {"confidence": score}
    s.trend = {"confidence": score}

    sessions.append(s)

ranked = engine.rank(sessions)

for trade in ranked:
    print(trade["symbol"], trade["score"])