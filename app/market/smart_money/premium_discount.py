def premium_discount_zone(
    current_price,
    swing_high,
    swing_low
):
    """
    Determine whether price is in
    Premium or Discount.
    """

    equilibrium = (
        swing_high +
        swing_low
    ) / 2

    if current_price > equilibrium:

        zone = "Premium"

    elif current_price < equilibrium:

        zone = "Discount"

    else:

        zone = "Equilibrium"

    return {

        "zone": zone,

        "equilibrium": equilibrium

    }