from app.analysis.scoring import (
    calculate_score,
    get_grade
)

from app.decision.actions import (
    decide_action
)

from app.decision.confidence import (
    calculate_confidence
)

from app.decision.filters import (
    apply_filters
)

from app.decision.reasons import (
    build_reasons
)


def make_decision(
    indicators,
    bullish,
    volume,
    alignment,
    pattern
):
    """
    Main Decision Engine.

    Returns everything needed to
    evaluate a trading opportunity.
    """

    volume_score = volume["score"]

    atr = indicators.get("atr", 0)

    # -----------------------------
    # Apply Filters
    # -----------------------------

    passed, filter_messages = apply_filters(
        indicators,
        bullish,
        volume_score,
        alignment,
        atr
    )

    if not passed:

        return {
            "action": "NO TRADE",
            "score": 0,
            "grade": "Avoid",
            "confidence": 0,
            "breakdown": {},
            "reasons": filter_messages
        }

    # -----------------------------
    # Calculate Score
    # -----------------------------

    score_data = calculate_score(
        indicators,
        bullish,
        volume_score,
        alignment,
        pattern
    )

    score = score_data["score"]

    breakdown = score_data["breakdown"]

    # -----------------------------
    # Grade
    # -----------------------------

    grade = get_grade(
        score
    )

    # -----------------------------
    # Decision
    # -----------------------------

    action = decide_action(
        score,
        bullish
    )

    # -----------------------------
    # Confidence
    # -----------------------------

    confidence = calculate_confidence(
        score,
        volume_score,
        alignment,
        bullish
    )

    # -----------------------------
    # Reasons
    # -----------------------------

    reasons = build_reasons(
        indicators,
        bullish,
        volume,
        alignment,
        pattern
    )

    return {

        "action": action,

        "score": score,

        "grade": grade,

        "confidence": confidence,

        "breakdown": breakdown,

        "reasons": reasons
    }