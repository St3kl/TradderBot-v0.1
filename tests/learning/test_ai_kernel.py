from pprint import pprint

from app.ai.kernel.ai_kernel import AIKernel

kernel = AIKernel()

decision = kernel.think(

    strategy="TREND",

    context="TRENDING | NORMAL",

    confidence=80,

    risk=1

)

print()

print("="*40)

print("AI KERNEL")

print("="*40)

print()

pprint(decision)

print()

print("✓ THINK PASSED")