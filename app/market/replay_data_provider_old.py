from app.market.indicator_engine import IndicatorEngine


class ReplayDataProvider:

    @staticmethod
    def get(candles):

        opens = [
            float(c["open"])
            for c in candles
        ]

        highs = [
            float(c["high"])
            for c in candles
        ]

        lows = [
            float(c["low"])
            for c in candles
        ]

        closes = [
            float(c["close"])
            for c in candles
        ]

        volumes = [
            float(c["volume"])
            for c in candles
        ]

        return IndicatorEngine.calculate(

            opens=opens,
            highs=highs,
            lows=lows,
            closes=closes,
            volumes=volumes,

        )