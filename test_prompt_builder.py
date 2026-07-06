from app.core.registry import engine
from app.ai.prompt_builder import build_prompt

session = engine.analyze("BTCUSDT")

prompt = build_prompt(session)

print(prompt)