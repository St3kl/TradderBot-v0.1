from enum import Enum


class TradingMode(Enum):

    DEVELOPMENT = "DEVELOPMENT"

    PAPER = "PAPER"

    STAGING = "STAGING"

    LIVE = "LIVE"


class ProductionModeController:

    def __init__(self):

        self.mode = TradingMode.DEVELOPMENT

    def set_mode(self, mode):

        if isinstance(mode, TradingMode):

            self.mode = mode

        else:

            self.mode = TradingMode(mode)

    def get_mode(self):

        return self.mode

    def is_live(self):

        return self.mode == TradingMode.LIVE

    def print(self):

        print()

        print("=" * 60)
        print("PRODUCTION MODE")
        print("=" * 60)
        print()

        print("Mode :", self.mode.value)

        print("Live :", self.is_live())