def validate_trade(
    trade,
    smart_money,
    structure,
    volume,
    indicators
):
    """
    Validates whether a setup is worth trading.

    Returns:

    {
        valid,
        quality,
        warnings,
        reasons
    }
    """

    quality = 100

    warnings = []

    reasons = []

    # -----------------------------
    # Risk Reward
    # -----------------------------

    rr = trade["risk_reward"]
    
    print("RR:", rr)
    print("RR TYPE:", type(rr))

    if rr < 2:

        quality -= 20

        warnings.append(
            "Poor Risk/Reward"
        )

    else:

        reasons.append(
            "Good Risk/Reward"
        )

    # -----------------------------
    # Premium / Discount
    # -----------------------------

    zone = smart_money["premium_discount"]["zone"]

    if structure["trend"] == "Bullish":

        if zone != "Discount":

            quality -= 15

            warnings.append(
                "Buying in Premium Zone"
            )

        else:

            reasons.append(
                "Buying in Discount Zone"
            )

    else:

        if zone != "Premium":

            quality -= 15

            warnings.append(
                "Selling in Discount Zone"
            )

        else:

            reasons.append(
                "Selling in Premium Zone"
            )

    # -----------------------------
    # Volume
    # -----------------------------

    if volume["score"] < 15:

        quality -= 10

        warnings.append(
            "Weak Volume"
        )

    else:

        reasons.append(
            "Strong Volume"
        )

    # -----------------------------
    # ATR Filter
    # -----------------------------

    if indicators["atr"] <= 0:

        quality -= 10

        warnings.append(
            "Invalid ATR"
        )

    # -----------------------------
    # Final Decision
    # -----------------------------

    valid = quality >= 70

    return {

    "valid": valid,

    "confidence": quality,

    "score": quality,

    "warnings": warnings,

    "reasons": reasons

}