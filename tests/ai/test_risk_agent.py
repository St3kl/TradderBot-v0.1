from pprint import pprint

from app.ai.agents.risk_agent import RiskAgent

execution = {

    "risk": {

        "position": {

            "risk_amount": 250

        }

    }

}

portfolio = {

    "drawdown": 12,

    "exposure": 60

}

agent = RiskAgent()

print()

print("=" * 40)

print("RISK AGENT")

print("=" * 40)

print()

pprint(

    agent.evaluate(

        execution,

        portfolio

    )

)

print()

print("✓ TEST PASSED")