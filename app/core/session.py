from datetime import datetime
from app.models.trade_plan import TradePlan


class TradingSession:

    def __init__(self):

        # ==========================================================
        # GENERAL
        # ==========================================================

        self.id = None
        self.symbol = ""
        self.timestamp = datetime.utcnow()

        # ==========================================================
        # MARKET
        # ==========================================================

        self.market_regime = {
            "regime": "UNKNOWN",
            "volatility": "UNKNOWN"
        }

        self.indicators = {}
        self.mtf = {}
        
        # =====================================================
        # MARKET REPORT
        # =====================================================

        self.market = {}

        # ==========================================================
        # STRATEGY
        # ==========================================================

        self.strategy = "DEFAULT"
        self.strategy_rules = {}

        # ==========================================================
        # TREND
        # ==========================================================

        self.trend = {
            "direction": "UNKNOWN",
            "bullish": False,
            "strength": 0,
            "confidence": 0
        }

        self.bullish = False

        # ==========================================================
        # PATTERNS
        # ==========================================================

        self.patterns = {
            "detected": [],
            "primary": None,
            "confidence": 0
        }

        # ==========================================================
        # STRUCTURE
        # ==========================================================

        self.structure = {
            "trend": "UNKNOWN",
            "bos": False,
            "choch": False
        }

        # ==========================================================
        # SMART MONEY
        # ==========================================================

        self.smart_money = {
            "order_blocks": {
                "bullish": 0,
                "bearish": 0
            },
            "fair_value_gaps": {
                "bullish": 0,
                "bearish": 0
            },
            "liquidity_sweep": {
                "buy_side": False,
                "sell_side": False
            },
            "score": 0
        }

        # ==========================================================
        # VOLUME
        # ==========================================================

        self.volume = {
            "status": "UNKNOWN",
            "score": 0,
            "strength": 0
        }

        # ==========================================================
        # SUPPORT / RESISTANCE
        # ==========================================================

        self.sr = {
            "support": None,
            "resistance": None
        }

        # ==========================================================
        # TRADE
        # ==========================================================

        self.trade_plan = TradePlan()

        # ==========================================================
        # CONFLUENCE
        # ==========================================================

        self.confluence = {
            "score": 0,
            "signals": []
        }

        # ==========================================================
        # VALIDATION
        # ==========================================================

        self.validation = {
            "valid": False,
            "confidence": 0,
            "score": 0,
            "reasons": []
        }

        # ==========================================================
        # CHECKLIST
        # ==========================================================

        self.checklist = {
            "passed": [],
            "failed": []
        }

        # ==========================================================
        # DECISION
        # ==========================================================

        self.decision = {
            "action": "WAIT",
            "confidence": 0,
            "reason": ""
        }

        # ==========================================================
        # EXECUTION
        # ==========================================================

        self.execution = {
            "approved": False,
            "confirmed": False,
            "executed": False,
            "paper_trade_id": None,
            "live_order_id": None,
            "status": "PENDING"
        }

        # ==========================================================
        # AI
        # ==========================================================

        self.ai = {
            "context": {},
            "reasoning": [],
            "prompt": "",
            "response": "",
            "report": ""
        }

        # compatibility

        self.ai_context = self.ai["context"]
        self.ai_reasoning = self.ai["reasoning"]
        self.ai_prompt = self.ai["prompt"]
        self.ai_response = self.ai["response"]
        self.ai_report = self.ai["report"]

        # ==========================================================
        # LEARNING
        # ==========================================================

        self.learning = {
            "recommendation": {},
            "optimization": {},
            "adaptive_parameters": {}
        }

        # ==========================================================
        # MEMORY
        # ==========================================================

        self.memory = {}
        
        # -------------------------------------------------
        # Compatibility aliases
        # -------------------------------------------------

        self.pattern = self.patterns
        self.support_resistance = self.sr
        self.trade = {

            "entry": None,

            "stop_loss": None,

            "take_profit": None,

            "risk_reward": 0,

            "position_size": 0,

            "risk_amount": 0

        }

        self.validation = {

            "valid": False,

            "confidence": 0,

            "score": 0,

            "reasons": [],

            "warnings": []

        }

        self.decision = {

            "action": "WAIT",

            "reason": "Not evaluated",

            "confidence": 0

        }

        self.ai = {

            "confidence": 0,

            "context": {},

            "reasoning": [],

            "response": ""

        }
        
        self.trade_quality = {
            "score": 0,
            "grade": "D"
        }

        self.errors = []
        
        
        balance: float = 10000
        # ==========================================================
        # REPORT
        # ==========================================================

        self.tf_report = {}
        self.report = ""