def build_prompt(context):
    """
    Converts the AI context into a structured prompt
    for the LLM.
    """

    market = context["market"]
    technical = context["technical"]
    smart = context["smart_money"]
    decision = context["decision"]
    validation = context["validation"]
    reasoning = context["reasoning"]

    prompt = f"""
You are an institutional trader.

Analyze the following setup exactly as a professional
fund manager.

========================
MARKET
========================

Symbol:
{context["symbol"]}

Current Price:
{market["price"]}

EMA50:
{market["ema50"]}

EMA200:
{market["ema200"]}

RSI:
{market["rsi"]}

ATR:
{market["atr"]}

========================
TECHNICAL
========================

Trend:
{technical["trend"]}

Pattern:
{technical["pattern"]}

Volume:
{technical["volume"]["strength"]}

MTF Alignment:
{technical["alignment"]}

========================
SMART MONEY
========================

Equal Highs:
{smart["liquidity"]["equal_highs"]}

Equal Lows:
{smart["liquidity"]["equal_lows"]}

Bullish OB:
{smart["order_blocks"]["bullish"]}

Bearish OB:
{smart["order_blocks"]["bearish"]}

Bullish FVG:
{smart["fair_value_gaps"]["bullish"]}

Bearish FVG:
{smart["fair_value_gaps"]["bearish"]}

Liquidity Sweep:
{smart["liquidity_sweep"]["type"]}

Premium / Discount:
{smart["premium_discount"]["zone"]}

========================
DECISION
========================

Action:
{decision["action"]}

Confidence:
{decision["confidence"]}

Score:
{decision["score"]}

Risk:
{decision["risk"]}

========================
VALIDATION
========================

Quality:
{validation["quality"]}

Valid:
{validation["valid"]}

========================
REASONING
========================

{reasoning}

========================
TASK
========================

Write:

1. Overall market narrative.

2. Explain WHY this trade exists.

3. Mention institutional activity.

4. Mention risks.

5. Mention invalidation.

6. Mention best execution idea.

Keep it under 250 words.

Use professional language.
"""

    return prompt