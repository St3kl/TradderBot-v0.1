class WalkForwardOptimizer:
    """
    Splits historical data into
    rolling train/test windows.
    """

    def split(

        self,

        candles,

        train_size,

        test_size

    ):

        windows = []

        start = 0

        while start + train_size + test_size <= len(candles):

            train = candles[
                start:start + train_size
            ]

            test = candles[
                start + train_size:
                start + train_size + test_size
            ]

            windows.append({

                "train": train,

                "test": test

            })

            start += test_size

        return windows