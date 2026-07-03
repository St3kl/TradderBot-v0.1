class TradingSession:

    def __init__(self):

        # --------------------------
        # General
        # --------------------------

        self.symbol = ""

        self.timestamp = None

        # --------------------------
        # Market Data
        # --------------------------

        self.indicators = {}

        self.mtf = {}

        # --------------------------
        # Trend
        # --------------------------

        self.trend = {
            "direction": "Unknown",
            "bullish": False,
            "strength": 0,
            "confidence": 0
        }

        # Compatibility
        self.bullish = False

        # --------------------------
        # Pattern Analysis
        # --------------------------

        self.patterns = {
            "detected": [],
            "primary": None,
            "confidence": 0
        }

        # --------------------------
        # Market Structure
        # --------------------------

        self.structure = {
            "trend": "Unknown",
            "bos": False,
            "choch": False
        }

        # --------------------------
        # Smart Money
        # --------------------------

        self.smart_money = {
            "order_blocks": [],
            "fvg": [],
            "liquidity": [],
            "score": 0
        }

        # --------------------------
        # Volume
        # --------------------------

        self.volume = {
            "status": "Unknown",
            "strength": 0
        }

        # --------------------------
        # Support / Resistance
        # --------------------------

        self.sr = {
            "support": None,
            "resistance": None
        }

        # --------------------------
        # Trade
        # --------------------------

        self.trade = {
            "entry": None,
            "stop_loss": None,
            "take_profit": None,
            "risk_reward": 0
        }

        # --------------------------
        # Confluence
        # --------------------------

        self.confluence = {
            "score": 0,
            "signals": []
        }

        # --------------------------
        # Decision
        # --------------------------

        self.decision = {
            "action": "WAIT",
            "confidence": 0
        }

        # --------------------------
        # Validation
        # --------------------------

        self.validation = {
            "valid": False,
            "confidence": 0,
            "score": 0,
            "reasons": []
        }

        # --------------------------
        # Checklist
        # --------------------------

        self.checklist = {
            "passed": [],
            "failed": []
        }

        # --------------------------
        # Reports
        # --------------------------

        self.tf_report = {}

        self.report = ""

        # --------------------------
        # AI
        # --------------------------

        self.ai_context = {}

        self.ai_reasoning = []

        self.ai_prompt = ""

        self.ai_response = ""

        self.ai_report = ""

        # --------------------------
        # Memory
        # --------------------------

        self.memory = {}