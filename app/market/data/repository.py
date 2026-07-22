from pathlib import Path

import pandas as pd


class MarketDataRepository:
    """
    Handles reading and writing market datasets.
    """

    ROOT = Path("data")

    def _filename(
        self,
        symbol,
        timeframe
    ):

        folder = self.ROOT / symbol.upper()

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        return folder / f"{symbol.upper()}_{timeframe.upper()}.csv"

    # ----------------------------------

    def save(

        self,
        symbol,
        timeframe,
        dataframe

    ):

        filename = self._filename(

            symbol,
            timeframe

        )

        dataframe.to_csv(

            filename,

            index=False

        )

        return filename

    # ----------------------------------

    def load(

        self,
        symbol,
        timeframe

    ):

        filename = self._filename(

            symbol,
            timeframe

        )

        if not filename.exists():

            return None

        return pd.read_csv(

            filename,

            parse_dates=["time"]

        )

    # ----------------------------------

    def exists(

        self,
        symbol,
        timeframe

    ):

        return self._filename(

            symbol,
            timeframe

        ).exists()