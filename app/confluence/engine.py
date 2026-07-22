from app.confluence.trend_score import calculate_trend_score
from app.confluence.pattern_score import calculate_pattern_score
from app.confluence.smart_money_score import calculate_smart_money_score
from app.confluence.volume_score import calculate_volume_score
from app.confluence.timeframe_score import calculate_timeframe_score
from app.confluence.risk_score import calculate_risk_score


def calculate_confluence(
    bullish,
    pattern,
    structure,
    volume,
    alignment,
    smart_money,
    validation=None,
):
    """
    Institutional Confluence Engine

    Every scoring module is evaluated independently and
    then aggregated into a final institutional score.
    """

    validation = validation or {
        "valid": False
    }

    trend = calculate_trend_score(
        bullish,
        structure
    )

    pattern_result = calculate_pattern_score(
        pattern
    )

    smart_money_result = calculate_smart_money_score(
        smart_money
    )

    volume_result = calculate_volume_score(
        volume
    )

    timeframe_result = calculate_timeframe_score(
        alignment
    )

    risk_result = calculate_risk_score(
        validation
    )

    modules = [

        trend,
        pattern_result,
        smart_money_result,
        volume_result,
        timeframe_result,
        risk_result

    ]

    total_score = sum(
        module["score"]
        for module in modules
    )

    signals = []

    missing = []

    for module in modules:

        signals.extend(
            module["signals"]
        )

        missing.extend(
            module["missing"]
        )

    # ---------------------------------------
    # Overall Strength
    # ---------------------------------------

    if total_score >= 85:

        strength = "Very Strong"

    elif total_score >= 70:

        strength = "Strong"

    elif total_score >= 55:

        strength = "Moderate"

    elif total_score >= 40:

        strength = "Weak"

    else:

        strength = "Very Weak"

    confidence = min(
        total_score,
        100
    )

    return {

        "score": total_score,

        "confidence": confidence,

        "strength": strength,

        "signals": signals,

        "missing": missing,

        "modules": {

            "trend": trend,

            "pattern": pattern_result,

            "smart_money": smart_money_result,

            "volume": volume_result,

            "timeframe": timeframe_result,

            "risk": risk_result

        }

    }