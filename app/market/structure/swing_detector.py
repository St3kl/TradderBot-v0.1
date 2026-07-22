from .models import SwingPoint


class SwingDetector:

    def detect(
        self,
        highs,
        lows,
        lookback=3
    ):

        swing_highs = []
        swing_lows = []

        for i in range(lookback, len(highs) - lookback):

            # Swing High
            if highs[i] == max(
                highs[i - lookback:i + lookback + 1]
            ):

                swing_highs.append(

                    SwingPoint(

                        index=i,

                        price=highs[i],

                        kind="HIGH"

                    )

                )

            # Swing Low
            if lows[i] == min(
                lows[i - lookback:i + lookback + 1]
            ):

                swing_lows.append(

                    SwingPoint(

                        index=i,

                        price=lows[i],

                        kind="LOW"

                    )

                )

        return swing_highs, swing_lows