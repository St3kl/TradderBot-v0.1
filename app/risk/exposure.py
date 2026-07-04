def analyze_exposure(open_positions):
    """
    Analyze portfolio directional exposure.

    Each position:

    {
        "symbol": "...",
        "direction": "LONG" or "SHORT",
        "risk": 100
    }
    """

    long_risk = 0
    short_risk = 0

    for position in open_positions:

        if position["direction"] == "LONG":
            long_risk += position["risk"]

        else:
            short_risk += position["risk"]

    total = long_risk + short_risk

    return {

        "long_risk": round(long_risk, 2),

        "short_risk": round(short_risk, 2),

        "net_exposure": round(long_risk - short_risk, 2),

        "total_exposure": round(total, 2)

    }