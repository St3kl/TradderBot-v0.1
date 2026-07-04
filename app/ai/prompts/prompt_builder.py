from app.ai.prompts.system_prompt import SYSTEM_PROMPT


def build_prompt(context):
    """
    Builds the complete prompt that will be sent
    to the LLM.
    """

    prompt = f"""
{SYSTEM_PROMPT}

==================================================
MARKET
==================================================

Symbol:
{context["symbol"]}

Price:
{context["market"]["price"]}

Trend:
{context["technical"]["trend"]}

RSI:
{context["market"]["rsi"]}

ATR:
{context["market"]["atr"]}

==================================================
SMART MONEY
==================================================

{context["smart_money"]}

==================================================
TRADE
==================================================

Entry:
{context["trade"]["entry"]}

Stop Loss:
{context["trade"]["stop_loss"]}

Take Profit:
{context["trade"]["take_profit"]}

Risk Reward:
{context["trade"]["risk_reward"]}

==================================================
DECISION
==================================================

{context["decision"]}

==================================================
VALIDATION
==================================================

{context["validation"]}

==================================================
CHECKLIST
==================================================

{context["checklist"]}

==================================================
REASONING
==================================================

"""

    for line in context["reasoning"]:
        prompt += f"- {line}\n"

    prompt += """
    
=== Historical Context ===

Previous Analysis:
{comparison}

Market Evolution:
{evolution}    

==================================================
TASK
==================================================

Write a professional trading report.

Explain:

• Current market condition
• Smart Money interpretation
• Whether the setup is valid
• Main risks
• Final recommendation

"""

    return prompt