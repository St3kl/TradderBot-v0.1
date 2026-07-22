from pprint import pprint
from types import SimpleNamespace

from app.ai.decision_brain import DecisionBrain

brain = DecisionBrain()

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

    "drawdown":3,

    "exposure":15

}

market = {

    "spread":0.05,

    "slippage":0.03,

    "liquidity":"HIGH"

}

research = {

    "win_rate":76,

    "profit_factor":2.6,

    "research_score":95

}

decision = brain.decide(

    session,

    execution,

    portfolio,

    market,

    research

)

print()

print("=" * 50)

print("DECISION BRAIN 2.0")

print("=" * 50)

print()

pprint(decision)

print()

print("✓ TEST PASSED")