from app.market.indicators import get_market_indicators
from app.market.forex_indicators import get_forex_indicators

from app.market.patterns.detector import detect_pattern
from app.market.patterns.support_resistance import find_support_resistance

from app.market.structure.structure import analyze_structure
from app.market.smart_money.engine import analyze_smart_money

from app.risk.calculator import calculate_trade_levels

from app.analysis.multi_timeframe import (
    analyze_timeframes,
    calculate_alignment,
)
from app.market.multi_timeframe import MultiTimeframeEngine

from app.analysis.volume import analyze_volume

from app.decision.engine import make_decision

from app.reports.report_builder import build_report

from app.confluence.engine import calculate_confluence

from app.validation.trade_validator import validate_trade

from app.checklist.institutional_checklist import build_checklist

from app.ai.context_builder import build_ai_context
from app.ai.narrator import build_market_story


def analyze_symbol(symbol):

    symbol = symbol.upper()

    # -------------------------------------------------
    # Load Market Data
    # -------------------------------------------------

    if symbol.endswith("USDT"):

        indicators = get_market_indicators(symbol)
        mtf = analyze_timeframes(symbol)

    else:

        forex_symbol = symbol[:3] + "/" + symbol[3:]

        indicators = get_forex_indicators(forex_symbol)
        mtf = None

    # -------------------------------------------------
    # Pattern Detection
    # -------------------------------------------------

    pattern = detect_pattern(indicators)

    # -------------------------------------------------
    # Volume
    # -------------------------------------------------

    if "volumes" in indicators:

        volume = analyze_volume(indicators["volumes"])

    else:

        volume = {
            "strength": "N/A",
            "score": 10,
        }

    # -------------------------------------------------
    # Trend
    # -------------------------------------------------

    bullish = indicators["ema50"] > indicators["ema200"]

    # -------------------------------------------------
    # Support / Resistance
    # -------------------------------------------------

    sr = find_support_resistance(indicators["closes"])

    # -------------------------------------------------
    # Trade Levels
    # -------------------------------------------------

    trade = calculate_trade_levels(
        indicators["price"],
        sr["support"],
        sr["resistance"],
        bullish,
        indicators.get("atr", 0),
    )

    # -------------------------------------------------
    # Market Structure
    # -------------------------------------------------

    structure = analyze_structure(
        indicators["highs"],
        indicators["lows"],
        indicators["closes"],
        bullish,
    )

    # -------------------------------------------------
    # Smart Money
    # -------------------------------------------------

    smart_money = analyze_smart_money(
        opens=indicators["opens"],
        highs=indicators["highs"],
        lows=indicators["lows"],
        closes=indicators["closes"],
        current_price=indicators["price"],
        swing_high=sr["resistance"],
        swing_low=sr["support"],
    )

    # -------------------------------------------------
    # Multi-Timeframe
    # -------------------------------------------------

    # if mtf:

    #     alignment = calculate_alignment(mtf)

    #     tf_report = ""

    #     for tf, info in mtf.items():

    #         tf_report += (
    #             f"{tf}: "
    #             f"{'Bullish' if info['bullish'] else 'Bearish'}\n"
    #         )

    # else:

    #     alignment = 0
    #     tf_report = "Forex MTF Coming Soon\n"
    mtf = MultiTimeframeEngine()

    results = mtf.analyze(symbol)

    alignment = mtf.alignment(results)

    confidence = mtf.confidence(alignment)

    # -------------------------------------------------
    # Confluence
    # -------------------------------------------------

    confluence = calculate_confluence(
        bullish,
        pattern,
        structure,
        volume,
        alignment,
        smart_money,
    )

    # -------------------------------------------------
    # Decision
    # -------------------------------------------------

    decision = make_decision(confluence)

    # -------------------------------------------------
    # Validation
    # -------------------------------------------------

    validation = validate_trade(
        trade,
        smart_money,
        structure,
        volume,
        indicators,
    )

    # -------------------------------------------------
    # Institutional Checklist
    # -------------------------------------------------

    checklist = build_checklist(
        bullish,
        structure,
        smart_money,
        volume,
        trade,
    )

    # -------------------------------------------------
    # AI Context
    # -------------------------------------------------

    ai_context = build_ai_context(
        symbol=symbol,
        indicators=indicators,
        decision=decision,
        trade=trade,
        structure=structure,
        smart_money=smart_money,
        pattern=pattern,
        volume=volume,
        validation=validation,
        checklist=checklist,
        tf_report=tf_report,
        alignment=alignment,
        confluence=confluence,
    )

    story = build_market_story(ai_context)

    # -------------------------------------------------
    # Final Report
    # -------------------------------------------------

    reports = build_report(
        symbol=symbol,
        tf_report=tf_report,
        decision=decision,
        alignment=alignment,
        pattern=pattern,
        sr=sr,
        trade=trade,
        indicators=indicators,
        volume=volume,
        structure=structure,
        smart_money=smart_money,
        validation=validation,
        checklist=checklist,
        story=story,
    )

    return reports