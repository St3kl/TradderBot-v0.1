def build_market_story(
    symbol,
    decision,
    structure,
    smart_money,
    pattern,
    volume,
    validation
):
    """
    Generates a professional market narrative.
    """

    story = []

    story.append(
        f"{symbol} is currently in a {structure['trend'].lower()} market structure."
    )

    if structure["bos"]["type"] == "Bullish BOS":
        story.append(
            "A bullish Break of Structure confirms buyers remain in control."
        )

    elif structure["bos"]["type"] == "Bearish BOS":
        story.append(
            "A bearish Break of Structure suggests sellers remain dominant."
        )

    zone = smart_money["premium_discount"]["zone"]

    if zone == "Discount":
        story.append(
            "Price is trading inside the institutional discount zone."
        )
    else:
        story.append(
            "Price is trading in premium territory."
        )

    if smart_money["order_blocks"]["bullish"] > 0:
        story.append(
            "Bullish order blocks are still active."
        )

    if smart_money["fair_value_gaps"]["bullish"] > 0:
        story.append(
            "Bullish Fair Value Gaps remain unfilled."
        )

    if volume["score"] >= 15:
        story.append(
            "Volume confirms participation."
        )

    if pattern != "No Strong Pattern":
        story.append(
            f"The latest price action formed a {pattern}."
        )

    if validation["valid"]:
        story.append(
            "Overall, this setup satisfies the institutional checklist."
        )
    else:
        story.append(
            "Several institutional confirmations are still missing."
        )

    story.append(
        f"Current recommendation: {decision['action']}."
    )

    return " ".join(story)