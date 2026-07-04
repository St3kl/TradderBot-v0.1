def compare_sessions(previous, current):

    comparison = {

        "price_change": 0,

        "confidence_change": 0,

        "trend_changed": False,

        "decision_changed": False,

        "summary": []

    }

    # -------------------------
    # Price
    # -------------------------

    previous_price = previous.get("price", 0)
    current_price = current.get("price", 0)

    comparison["price_change"] = round(
        current_price - previous_price,
        2
    )

    # -------------------------
    # Confidence
    # -------------------------

    previous_conf = previous.get("confidence", 0)
    current_conf = current.get("confidence", 0)

    comparison["confidence_change"] = (
        current_conf - previous_conf
    )

    # -------------------------
    # Trend
    # -------------------------

    previous_trend = previous["trend"]["direction"]
    current_trend = current["trend"]["direction"]

    comparison["trend_changed"] = (
        previous_trend != current_trend
    )

    # -------------------------
    # Decision
    # -------------------------

    previous_action = previous["decision"]["action"]
    current_action = current["decision"]["action"]

    comparison["decision_changed"] = (
        previous_action != current_action
    )

    # -------------------------
    # Human Summary
    # -------------------------

    if comparison["price_change"] > 0:
        comparison["summary"].append(
            f"Price increased by {comparison['price_change']}"
        )

    elif comparison["price_change"] < 0:
        comparison["summary"].append(
            f"Price decreased by {abs(comparison['price_change'])}"
        )

    if comparison["confidence_change"] > 0:
        comparison["summary"].append(
            "Confidence improved."
        )

    elif comparison["confidence_change"] < 0:
        comparison["summary"].append(
            "Confidence weakened."
        )

    if comparison["trend_changed"]:
        comparison["summary"].append(
            "Trend changed."
        )

    if comparison["decision_changed"]:
        comparison["summary"].append(
            "Trading decision changed."
        )

    return comparison