import requests

from app.market.indicator_engine import IndicatorEngine


def get_market_indicators(
    symbol,
    interval="1h"
):

    url = (
        "https://api.binance.com/api/v3/klines"
        f"?symbol={symbol}"
        f"&interval={interval}"
        f"&limit=200"
    )

    try:

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

    except requests.exceptions.RequestException as e:

        raise Exception(
            f"Unable to connect to Binance:\n{e}"
        )

    opens = [
        float(candle[1])
        for candle in data
    ]

    highs = [
        float(candle[2])
        for candle in data
    ]

    lows = [
        float(candle[3])
        for candle in data
    ]

    closes = [
        float(candle[4])
        for candle in data
    ]

    volumes = [
        float(candle[5])
        for candle in data
    ]

    return IndicatorEngine.calculate(

        opens=opens,

        highs=highs,

        lows=lows,

        closes=closes,

        volumes=volumes,

    )