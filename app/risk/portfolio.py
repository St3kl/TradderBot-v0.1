def calculate_portfolio_risk(open_positions):
    """
    Calculates the total portfolio exposure.

    open_positions example:

    [
        {"symbol":"BTC","risk":100},
        {"symbol":"ETH","risk":80}
    ]
    """

    total_risk = 0

    for position in open_positions:

        total_risk += position["risk"]

    return {

        "positions": len(open_positions),

        "total_risk": round(total_risk, 2)

    }