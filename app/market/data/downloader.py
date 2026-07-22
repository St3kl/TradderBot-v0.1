import requests
import pandas as pd


class BinanceDownloader:
    """
    Downloads historical candles from Binance.
    """

    BASE_URL = "https://api.binance.com/api/v3/klines"

    def download(
        self,
        symbol,
        timeframe,
        limit=1000
    ):

        params = {
            "symbol": symbol.upper(),
            "interval": timeframe.lower(),
            "limit": limit
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=20
        )

        response.raise_for_status()

        candles = response.json()

        rows = []

        for candle in candles:

            rows.append({

                "time": pd.to_datetime(
                    candle[0],
                    unit="ms"
                ),

                "open": float(candle[1]),
                "high": float(candle[2]),
                "low": float(candle[3]),
                "close": float(candle[4]),
                "volume": float(candle[5])

            })

        return pd.DataFrame(rows)