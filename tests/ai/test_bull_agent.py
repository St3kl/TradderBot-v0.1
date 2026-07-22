from pprint import pprint

from types import SimpleNamespace

from app.ai.agents.bull_agent import BullAgent

session = SimpleNamespace(

    bullish=True,

    trend=True,

    volume=True

)

agent = BullAgent()

print()

print("="*40)

print("BULL AGENT")

print("="*40)

print()

pprint(

    agent.evaluate(session)

)

print()

print("✓ TEST PASSED")