def build_checklist(
    bullish,
    structure,
    smart_money,
    volume,
    trade
):
    """
    Institutional Trade Checklist
    """

    checklist = {}

    checklist["EMA Trend"] = bullish

    checklist["Market Structure"] = (
        structure["trend"] == "Bullish"
    )

    checklist["Bullish BOS"] = (
        structure["bos"]["type"] == "Bullish BOS"
    )

    checklist["Bullish CHoCH"] = (
        structure["choch"]["type"] == "Bullish CHoCH"
    )

    checklist["Discount Zone"] = (
        smart_money["premium_discount"]["zone"]
        == "Discount"
    )

    checklist["Order Block"] = (
        smart_money["order_blocks"]["bullish"] > 0
    )

    checklist["Fair Value Gap"] = (
        smart_money["fair_value_gaps"]["bullish"] > 0
    )

    checklist["Strong Volume"] = (
        volume["score"] >= 15
    )

    checklist["Good Risk Reward"] = (
        trade["risk_reward"] >= 2
    )

    return checklist