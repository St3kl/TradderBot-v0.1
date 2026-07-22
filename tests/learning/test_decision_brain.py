from pprint import pprint

from app.ai.brain.decision_brain import DecisionBrain

brain = DecisionBrain()

decision = brain.think(

    strategy="TREND",

    context="TREND performs best during TRENDING | NORMAL",

    confidence=82,

    risk=1

)

print()

print("=" * 30)

print("DECISION BRAIN")

print("=" * 30)

print()

pprint(decision)

print()

print("✓ TEST PASSED")