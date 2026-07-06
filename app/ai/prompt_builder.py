from app.ai.context.context_builder import build_ai_context
from app.ai.reasoning.reasoning_engine import build_reasoning


def build_prompt(session):

    context = build_ai_context(session)

    reasoning = build_reasoning(context)

    prompt = f"""
You are an institutional trader.

Analyze the following market.

Market Context

{context}

Institutional Reasoning

"""

    for item in reasoning:

        prompt += f"- {item}\n"

    prompt += """

Provide:

1. Market Summary

2. Why this trade is valid or invalid

3. Risk Assessment

4. Institutional Opinion

5. Final Recommendation

"""

    return prompt