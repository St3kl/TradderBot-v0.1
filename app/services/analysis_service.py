from app.market.indicators import get_market_indicators
from app.market.forex_indicators import get_forex_indicators

from app.patterns.detector import detect_pattern
from app.patterns.support_resistance import find_support_resistance

from app.risk.calculator import calculate_trade_levels

from app.analysis.multi_timeframe import (
    analyze_timeframes,
    calculate_alignment,
    alignment_confidence
)

from app.analysis.volume import analyze_volume

from app.analysis.scoring import (
    calculate_score,
    get_grade
)

from app.reports.report_builder import (
    build_report
)


def analyze_symbol(symbol):

    symbol = symbol.upper()

    # -----------------------------
    # Load Market
    # -----------------------------

    if symbol.endswith("USDT"):

        indicators = get_market_indicators(symbol)

        mtf = analyze_timeframes(symbol)

    else:

        forex_symbol = (
            symbol[:3] +
            "/" +
            symbol[3:]
        )

        indicators = get_forex_indicators(
            forex_symbol
        )

        mtf = None

    # -----------------------------
    # Pattern
    # -----------------------------

    pattern = detect_pattern(
        indicators
    )

    # -----------------------------
    # Volume
    # -----------------------------

    if "volumes" in indicators:

        volume = analyze_volume(
            indicators["volumes"]
        )

        volume_score = volume["score"]

    else:

        volume = {
            "strength": "N/A",
            "score": 10
        }

        volume_score = 10

    # -----------------------------
    # Trend
    # -----------------------------

    bullish = (
        indicators["ema50"] >
        indicators["ema200"]
    )

    # -----------------------------
    # Support Resistance
    # -----------------------------

    sr = find_support_resistance(
        indicators["closes"]
    )

    # -----------------------------
    # Trade Levels
    # -----------------------------

    trade = calculate_trade_levels(
        indicators["price"],
        sr["support"],
        sr["resistance"],
        bullish,
        indicators.get("atr", 0)
    )

    # -----------------------------
    # Multi Timeframe
    # -----------------------------

    if mtf:

        alignment = calculate_alignment(
            mtf
        )

        confidence = alignment_confidence(
            alignment
        )

        tf_report = ""

        for tf, info in mtf.items():

            tf_report += (
                f"{tf}: "
                f"{'Bullish' if info['bullish'] else 'Bearish'}\n"
            )

    else:

        alignment = 0

        confidence = 75

        tf_report = "Forex MTF Coming Soon\n"

    # -----------------------------
    # Score
    # -----------------------------

    score_data = calculate_score(
        indicators,
        bullish,
        volume_score,
        alignment,
        pattern
    )

    score = score_data["score"]

    grade = get_grade(score)

    breakdown = score_data["breakdown"]

    # -----------------------------
    # Report
    # -----------------------------

    report = build_report(
        symbol=symbol,
        tf_report=tf_report,
        score=score,
        breakdown=breakdown,
        grade=grade,
        alignment=alignment,
        confidence=confidence,
        pattern=pattern,
        sr=sr,
        trade=trade,
        indicators=indicators,
        volume=volume
    )

    return report