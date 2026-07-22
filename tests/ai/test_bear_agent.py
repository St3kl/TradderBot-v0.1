from pprint import pprint
from types import SimpleNamespace

from app.ai.agents.bear_agent import BearAgent

session = SimpleNamespace(

    bearish=True,

    downtrend=True,

    sell_volume=True

)

agent = BearAgent()

print()

print("=" * 40)
print("BEAR AGENT")
print("=" * 40)
print()

pprint(

    agent.evaluate(session)

)

print()

print("✓ TEST PASSED")