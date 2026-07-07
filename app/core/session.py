class TradingSession:

    def __init__(self):

        # =====================================================
        # GENERAL
        # =====================================================

        self.symbol = ""
        self.timestamp = None

        # =====================================================
        # MARKET
        # =====================================================

        self.indicators = {}

        self.market_regime = {
            "regime": None,
            "volatility": None
        }

        self.mtf = {}

        # =====================================================
        # STRATEGY
        # =====================================================

        self.strategy = None
        self.strategy_rules = {}

        # =====================================================
        # TREND
        # =====================================================

        self.trend = {
            "direction": "Unknown",
            "bullish": False,
            "strength": 0,
            "confidence": 0
        }

        # -----------------------------------------------------
        # Temporary compatibility
        # Remove after all stages use session.trend["bullish"]
        # -----------------------------------------------------

        self.bullish = False

        # =====================================================
        # PATTERN ANALYSIS
        # =====================================================

        self.patterns = {
            "detected": [],
            "primary": None,
            "confidence": 0
        }

        # =====================================================
        # MARKET STRUCTURE
        # =====================================================

        self.structure = {
            "trend": "Unknown",
            "bos": False,
            "choch": False
        }

        # =====================================================
        # SMART MONEY CONCEPTS
        # =====================================================

        self.smart_money = {
            "order_blocks": [],
            "fvg": [],
            "liquidity": [],
            "score": 0
        }

        # =====================================================
        # VOLUME
        # =====================================================

        self.volume = {
            "status": "Unknown",
            "strength": 0
        }

        # =====================================================
        # SUPPORT / RESISTANCE
        # =====================================================

        self.sr = {
            "support": None,
            "resistance": None
        }

        # =====================================================
        # TRADE PLAN
        # =====================================================

        self.trade = {
            "entry": None,
            "stop_loss": None,
            "take_profit": None,
            "risk_reward": 0,
            "position_size": None
        }

        # =====================================================
        # CONFLUENCE
        # =====================================================

        self.confluence = {
            "score": 0,
            "signals": []
        }

        # =====================================================
        # DECISION
        # =====================================================

        self.decision = {
            "action": "WAIT",
            "confidence": 0
        }

        # =====================================================
        # VALIDATION
        # =====================================================

        self.validation = {
            "valid": False,
            "confidence": 0,
            "score": 0,
            "reasons": []
        }

        # =====================================================
        # CHECKLIST
        # =====================================================

        self.checklist = {
            "passed": [],
            "failed": []
        }

        # =====================================================
        # EXECUTION
        # =====================================================

        self.execution = {
            "executed": False,
            "paper_trade_id": None,
            "live_order_id": None,
            "status": "PENDING"
        }

        # =====================================================
        # AI
        # =====================================================

        self.ai = {
            "context": {},
            "reasoning": [],
            "prompt": "",
            "response": "",
            "report": ""
        }

        # -----------------------------------------------------
        # Temporary compatibility
        # Remove after migrating the project
        # -----------------------------------------------------

        self.ai_context = self.ai["context"]
        self.ai_reasoning = self.ai["reasoning"]
        self.ai_prompt = self.ai["prompt"]
        self.ai_response = self.ai["response"]
        self.ai_report = self.ai["report"]

        # =====================================================
        # MEMORY
        # =====================================================

        self.memory = {}

        # =====================================================
        # REPORTING
        # =====================================================

        self.tf_report = {}
        self.report = ""