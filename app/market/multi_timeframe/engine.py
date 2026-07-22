from app.market.indicators import get_market_indicators


class MultiTimeframeEngine:
    """
    Performs multi-timeframe market analysis.
    """

    DEFAULT_TIMEFRAMES = (
        "15m",
        "1h",
        "4h",
        "1d",
    )

    def analyze(
        self,
        symbol,
        timeframes=None,
    ):

        if timeframes is None:
            timeframes = self.DEFAULT_TIMEFRAMES

        results = {}

        for tf in timeframes:

            data = get_market_indicators(
                symbol,
                tf,
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

    # -------------------------------------

    def alignment(self, results):

        return sum(

            1

            for tf in results.values()

            if tf["bullish"]

        )

    # -------------------------------------

    def confidence(self, alignment):

        scores = {

            4: 90,

            3: 75,

            2: 55,

            1: 35,

            0: 20,

        }

        return scores.get(alignment, 0)