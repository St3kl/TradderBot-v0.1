from app.core.registry import engine

from app.ai.context.context_builder import build_ai_context
from app.ai.reasoning.reasoning_engine import build_reasoning
from app.ai.prompts.prompt_builder import build_prompt


# ----------------------------------------------------
# Run Trading Engine
# ----------------------------------------------------

session = engine.analyze("BTCUSDT")

# ----------------------------------------------------
# Debug Trading Session
# ----------------------------------------------------

print("\n========== SESSION ==========\n")

print("Symbol:", session.symbol)

print("\nIndicators:")
print(session.indicators)

print("\nBullish:")
print(session.bullish)

print("\nSupport / Resistance:")
print(session.sr)

print("\nTrade:")
print(session.trade)

print("\nStructure:")
print(session.structure)

print("\nSmart Money:")
print(session.smart_money)

print("\nVolume:")
print(session.volume)

print("\nAlignment:")
print(session.alignment)

print("\nMTF:")
print(session.mtf)

print("\nConfluence:")
print(session.confluence)

print("\nDecision:")
print(session.decision)

print("\nValidation:")
print(session.validation)

print("\nChecklist:")
print(session.checklist)


# ----------------------------------------------------
# Build AI Context
# ----------------------------------------------------

context = build_ai_context(session)

# ----------------------------------------------------
# Build Reasoning
# ----------------------------------------------------

context["reasoning"] = build_reasoning(context)

print("\n========== REASONING ==========\n")

for line in context["reasoning"]:
    print("-", line)

# ----------------------------------------------------
# Build Prompt
# ----------------------------------------------------

prompt = build_prompt(context)

print("\n========== PROMPT ==========\n")

print(prompt)

from app.core.registry import engine
from app.ai.engine import AIEngine

session = engine.analyze("BTCUSDT")

ai = AIEngine()

report = ai.analyze(session)

print(report)

from app.ai.llm.lmstudio_client import ask_lmstudio

print(
    ask_lmstudio(
        "Say hello."
    )
)