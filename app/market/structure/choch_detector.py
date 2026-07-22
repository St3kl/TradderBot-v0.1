class CHoCHDetector:

    def detect(

        self,

        closes,

        swing_highs,

        swing_lows,

        current_trend,

    ):

        bullish = False
        bearish = False

        # ------------------------
        # Bullish CHoCH
        # ------------------------

        if current_trend == "Bearish":

            if swing_highs:

                last_high = swing_highs[-1]

                if closes[-1] > last_high.price:

                    bullish = True

        # ------------------------
        # Bearish CHoCH
        # ------------------------

        elif current_trend == "Bullish":

            if swing_lows:

                last_low = swing_lows[-1]

                if closes[-1] < last_low.price:

                    bearish = True

        return {

            "bullish": bullish,

            "bearish": bearish

        }