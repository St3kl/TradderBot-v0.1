class IndicatorCache:
    """
    Holds a dataset with all indicators already computed.
    """

    def __init__(self):

        self.df = None

    # ----------------------------

    def load(self, dataframe):

        self.df = dataframe

    # ----------------------------

    def candle(self, index):

        return self.df.iloc[index].to_dict()

    # ----------------------------

    def size(self):

        if self.df is None:

            return 0

        return len(self.df)