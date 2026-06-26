from app.market.indicators import (
    get_market_indicators
)


def analyze_timeframes(
    symbol
):

    timeframes = [
        "15m",
        "1h",
        "4h",
        "1d"
    ]

    results = {}

    for tf in timeframes:

        data = get_market_indicators(
            symbol,
            tf
        )

        bullish = (
            data["ema50"] >
            data["ema200"]
        )

        results[tf] = {
            "bullish": bullish,
            "data": data
        }

    return results

def calculate_alignment(
    results
):

    bullish_count = sum(
        1
        for tf in results.values()
        if tf["bullish"]
    )

    return bullish_count


def alignment_confidence(
    alignment
):

    scores = {
        4: 90,
        3: 75,
        2: 55,
        1: 35,
        0: 20
    }

    return scores[alignment]