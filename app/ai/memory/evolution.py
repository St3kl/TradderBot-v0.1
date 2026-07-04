def analyze_market_evolution(history):

    if len(history) < 2:
        return None

    prices = [h["price"] for h in history]
    confidence = [h["confidence"] for h in history]
    decisions = [h["decision"]["action"] for h in history]
    trends = [h["trend"]["direction"] for h in history]

    evolution = {}

    # -------------------------
    # Price Trend
    # -------------------------

    if prices[-1] > prices[0]:
        evolution["price_trend"] = "Rising"
    elif prices[-1] < prices[0]:
        evolution["price_trend"] = "Falling"
    else:
        evolution["price_trend"] = "Sideways"

    # -------------------------
    # Confidence Trend
    # -------------------------

    if confidence[-1] > confidence[0]:
        evolution["confidence_trend"] = "Improving"
    elif confidence[-1] < confidence[0]:
        evolution["confidence_trend"] = "Weakening"
    else:
        evolution["confidence_trend"] = "Stable"

    # -------------------------
    # Trend Stability
    # -------------------------

    evolution["trend_stable"] = (
        len(set(trends)) == 1
    )

    # -------------------------
    # Decision Stability
    # -------------------------

    evolution["decision_stable"] = (
        len(set(decisions)) == 1
    )

    # -------------------------
    # Latest Decision
    # -------------------------

    evolution["current_decision"] = decisions[-1]

    # -------------------------
    # History Size
    # -------------------------

    evolution["samples"] = len(history)

    return evolution