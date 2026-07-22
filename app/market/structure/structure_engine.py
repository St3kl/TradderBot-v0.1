from .swing_detector import SwingDetector
from .bos_detector import BOSDetector
from .choch_detector import CHoCHDetector
from .trend_state import TrendState

from .models import StructureResult


class StructureEngine:

    def __init__(self):

        self.swings = SwingDetector()
        self.bos = BOSDetector()
        self.choch = CHoCHDetector()
        self.trend = TrendState()

    def analyze(

        self,

        highs,

        lows,

        closes,

    ):

        # ------------------------
        # Detect Swings
        # ------------------------

        swing_highs, swing_lows = self.swings.detect(
            highs,
            lows
        )

        # ------------------------
        # BOS
        # ------------------------

        bos = self.bos.detect(
            closes,
            swing_highs,
            swing_lows
        )

        # ------------------------
        # Initial Trend
        # ------------------------

        initial_trend = "Bullish"

        if bos["bearish"]:
            initial_trend = "Bearish"

        # ------------------------
        # CHoCH
        # ------------------------

        choch = self.choch.detect(
            closes,
            swing_highs,
            swing_lows,
            initial_trend
        )

        # ------------------------
        # Final Trend
        # ------------------------

        trend = self.trend.evaluate(
            bos,
            choch
        )

        return StructureResult(

            trend=trend["trend"],

            phase=trend["phase"],

            bullish_bos=bos["bullish"],

            bearish_bos=bos["bearish"],

            bullish_choch=choch["bullish"],

            bearish_choch=choch["bearish"],

            swing_highs=swing_highs,

            swing_lows=swing_lows,

            confidence=trend["confidence"]

        )