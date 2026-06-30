def build_market_story(ai_context):
    """
    Build the AI market narration from the AI context.
    """

    symbol = ai_context["symbol"]

    decision = ai_context["decision"]

    structure = ai_context["technical"]["trend"]

    pattern = ai_context["technical"]["pattern"]

    volume = ai_context["technical"]["volume"]

    smart_money = ai_context["smart_money"]

    validation = ai_context["validation"]

    story = f"""
The current market for {symbol} is showing a {structure.lower()} market structure.

The decision engine recommends a {decision["action"]} setup with a confidence of
{decision["confidence"]}% and an overall strength of
{decision["strength"]}.

Pattern detected:
{pattern}

Volume:
{volume["strength"]}

Institutional zone:
{smart_money["premium_discount"]["zone"]}

Trade Quality:
{validation["quality"]}/100
"""

    return story.strip()