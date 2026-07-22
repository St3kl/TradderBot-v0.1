from app.market.data.downloader import BinanceDownloader
from app.market.data.repository import MarketDataRepository
from app.market.data.validator import MarketDataValidator
from app.market.preprocessing.dataset_preprocessor import DatasetPreprocessor

class MarketDataManager:
    """
    Central market data manager.

    Responsible for:

    • Downloading
    • Validating
    • Saving
    • Loading
    """

    def __init__(self):

        self.downloader = BinanceDownloader()
        self.repository = MarketDataRepository()
        self.validator = MarketDataValidator()
        self.preprocessor = DatasetPreprocessor()

    # ---------------------------------

    def get_dataset(

        self,
        symbol,
        timeframe,
        limit=1000,
        refresh=False

    ):

        if (

            not refresh

            and

            self.repository.exists(

                symbol,
                timeframe

        )

    ):

            df = self.repository.load(

                symbol,
                timeframe

            )

        df = self.preprocessor.process(df)

        return df

        self.validator.validate(df)

        self.repository.save(

            symbol,
            timeframe,
            df

        )

        df = self.preprocessor.process(df)

        return df