class TrendState:

    def evaluate(

        self,

        bos,

        choch,

    ):

        # --------------------
        # Bullish Trend
        # --------------------

        if bos["bullish"]:

            trend = "Bullish"

            phase = "Expansion"

            confidence = 90

        # --------------------
        # Bearish Trend
        # --------------------

        elif bos["bearish"]:

            trend = "Bearish"

            phase = "Expansion"

            confidence = 90

        # --------------------
        # Transition
        # --------------------

        elif choch["bullish"]:

            trend = "Bullish"

            phase = "Transition"

            confidence = 65

        elif choch["bearish"]:

            trend = "Bearish"

            phase = "Transition"

            confidence = 65

        else:

            trend = "Range"

            phase = "Accumulation"

            confidence = 40

        return {

            "trend": trend,

            "phase": phase,

            "confidence": confidence

        }