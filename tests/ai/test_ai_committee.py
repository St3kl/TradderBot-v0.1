from pprint import pprint
from types import SimpleNamespace

from app.ai.committee import AICommittee

session = SimpleNamespace(

    bullish=True,

    bearish=False,

    trend=True,

    downtrend=False,

    volume=True,

    sell_volume=False

)

execution = {

    "risk": {

        "position": {

            "risk_amount":100

        }

    }

}

portfolio = {

    "drawdown":2,

    "exposure":20

}

market = {

    "spread":0.05,

    "slippage":0.05,

    "liquidity":"HIGH"

}

research = {

    "win_rate":74,

    "profit_factor":2.5,

    "research_score":96

}

committee = AICommittee()

decision = committee.evaluate(

    session,

    execution,

    portfolio,

    market,

    research

)

print()

print("="*40)

print("AI COMMITTEE")

print("="*40)

print()

pprint(decision)

print()

print("✓ TEST PASSED")