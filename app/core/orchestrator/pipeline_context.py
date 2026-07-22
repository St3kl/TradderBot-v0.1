class PipelineContext:
    """
    Shared context flowing through
    the complete AI pipeline.
    """

    def __init__(self):

        self.symbol = None

        self.session = None

        self.market = None

        self.research = None

        self.execution = None

        self.portfolio = None

        self.decision = None

        self.trade = None

        self.learning = None