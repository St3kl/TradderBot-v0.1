from .models import SwingPoint


class BOSDetector:

    def detect(
        self,
        closes,
        swing_highs,
        swing_lows
    ):

        bullish = False
        bearish = False

        bullish_price = None
        bearish_price = None

        # -----------------------------
        # Bullish BOS
        # -----------------------------

        if swing_highs:

            last_high = swing_highs[-1]

            if closes[-1] > last_high.price:

                bullish = True
                bullish_price = last_high.price

        # -----------------------------
        # Bearish BOS
        # -----------------------------

        if swing_lows:

            last_low = swing_lows[-1]

            if closes[-1] < last_low.price:

                bearish = True
                bearish_price = last_low.price

        return {

            "bullish": bullish,

            "bearish": bearish,

            "bullish_price": bullish_price,

            "bearish_price": bearish_price

        }