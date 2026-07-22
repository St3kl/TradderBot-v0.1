import pandas as pd


class MarketDataValidator:
    """
    Validates downloaded market datasets.
    """

    REQUIRED_COLUMNS = [

        "time",
        "open",
        "high",
        "low",
        "close",
        "volume"

    ]

    def validate(self, df):

        # -------------------------
        # Empty dataset
        # -------------------------

        if df.empty:

            raise ValueError(
                "Dataset is empty."
            )

        # -------------------------
        # Required columns
        # -------------------------

        missing = [

            c
            for c in self.REQUIRED_COLUMNS
            if c not in df.columns

        ]

        if missing:

            raise ValueError(
                f"Missing columns: {missing}"
            )

        # -------------------------
        # Null values
        # -------------------------

        if df.isnull().any().any():

            raise ValueError(
                "Dataset contains NULL values."
            )

        # -------------------------
        # Duplicate timestamps
        # -------------------------

        if df["time"].duplicated().any():

            raise ValueError(
                "Duplicate timestamps detected."
            )

        # -------------------------
        # OHLC consistency
        # -------------------------

        if (df["high"] < df["low"]).any():

            raise ValueError(
                "Invalid candle detected."
            )

        return True