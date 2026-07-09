from app.database.repositories.trade_repository import TradeRepository
from app.ai.memory.similarity_engine import SimilarityEngine
from app.ai.memory.vector_engine import VectorEngine


class MemoryEngine:
    """
    Central memory subsystem.

    Responsible for retrieving historical trades,
    generating vectors and finding similar trades.
    """

    def __init__(self):

        self.repository = TradeRepository()

        self.similarity = SimilarityEngine()

        self.vector = VectorEngine()

    # --------------------------------------------------
    # Trade History
    # --------------------------------------------------

    def history(self):

        return self.repository.get_all_trades()

    # --------------------------------------------------
    # Strategy Comparison
    # --------------------------------------------------

    def compare(self, symbol):

        trades = [

            t for t in self.history()

            if t["symbol"] == symbol

        ]

        if len(trades) < 2:

            return None

        return {

            "previous": trades[-2],

            "current": trades[-1]

        }

    # --------------------------------------------------
    # Market Evolution
    # --------------------------------------------------

    def evolution(self, symbol):

        trades = [

            t for t in self.history()

            if t["symbol"] == symbol

        ]

        return {

            "total_trades": len(trades),

            "wins": len(

                [t for t in trades if t.get("result") == "WIN"]

            ),

            "losses": len(

                [t for t in trades if t.get("result") == "LOSS"]

            )

        }

    # --------------------------------------------------
    # Vector
    # --------------------------------------------------

    def build_vector(self, context):

        return self.vector.build(context)

    # --------------------------------------------------
    # Similar Trade
    # --------------------------------------------------

    def similar_trade(

        self,

        symbol,

        vector

    ):

        return self.similarity.find_similar(

            symbol,

            vector

        )
        
        # --------------------------------------------------
    # Store Trade
    # --------------------------------------------------

    def store(self, trade):
        """
        Cache a completed trade.

        Persistence is handled by TradeRepository.
        MemoryEngine only manages learned knowledge.
        """

        print(f"Memory updated for {trade['symbol']}")     