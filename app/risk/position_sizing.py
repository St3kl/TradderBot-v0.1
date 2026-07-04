def calculate_position_size(
    balance,
    risk_percent,
    entry,
    stop_loss
):
    """
    Calculates the correct position size based on
    account balance and maximum risk.

    Returns:
        position_size
        risk_amount
        stop_distance
    """

    # -------------------------
    # Risk Capital
    # -------------------------

    risk_amount = balance * (risk_percent / 100)

    # -------------------------
    # Stop Distance
    # -------------------------

    stop_distance = abs(entry - stop_loss)

    if stop_distance <= 0:

        return {
            "position_size": 0,
            "risk_amount": risk_amount,
            "stop_distance": stop_distance
        }

    # -------------------------
    # Position Size
    # -------------------------

    position_size = risk_amount / stop_distance

    return {

        "position_size": round(position_size, 6),

        "risk_amount": round(risk_amount, 2),

        "stop_distance": round(stop_distance, 5)

    }