class PipelineDebugger:

    LINE = "=" * 70
    SEP = "-" * 70

    def print_session(self, session):

        print("\n")
        print(self.LINE)
        print("TRADDERBOT PIPELINE DEBUG")
        print(self.LINE)

        # =====================================================
        # GENERAL
        # =====================================================

        self.section("GENERAL")

        print(f"Symbol      : {session.symbol}")
        print(f"Timestamp   : {session.timestamp}")

        # =====================================================
        # MARKET
        # =====================================================

        self.section("MARKET")

        indicators = session.indicators

        print(f"Price       : {indicators.get('price')}")
        print(f"EMA50       : {indicators.get('ema50')}")
        print(f"EMA200      : {indicators.get('ema200')}")
        print(f"RSI         : {indicators.get('rsi')}")
        print(f"ATR         : {indicators.get('atr')}")

        if "volumes" in indicators:
            print(f"Candles     : {len(indicators['closes'])}")
            print(f"Volumes     : {len(indicators['volumes'])}")

        # =====================================================
        # MARKET REGIME
        # =====================================================

        self.section("MARKET REGIME")

        print(session.market_regime)

        # =====================================================
        # STRATEGY
        # =====================================================

        self.section("STRATEGY")

        print(session.strategy)

        if hasattr(session, "strategy_rules"):
            print(session.strategy_rules)

        # =====================================================
        # TREND
        # =====================================================

        self.section("TREND")

        print(session.trend)

        # =====================================================
        # PATTERNS
        # =====================================================

        self.section("PATTERNS")

        if hasattr(session, "patterns"):
            print(session.patterns)

        elif hasattr(session, "pattern"):
            print(session.pattern)

        # =====================================================
        # SUPPORT / RESISTANCE
        # =====================================================

        self.section("SUPPORT / RESISTANCE")

        print(session.sr)

        # =====================================================
        # TRADE
        # =====================================================

        self.section("TRADE")

        if hasattr(session, "trade"):
            print(session.trade)

        print(session.trade_plan)

        # =====================================================
        # STRUCTURE
        # =====================================================

        self.section("STRUCTURE")

        print(session.structure)

        # =====================================================
        # SMART MONEY
        # =====================================================

        self.section("SMART MONEY")

        print(session.smart_money)

        # =====================================================
        # VOLUME
        # =====================================================

        self.section("VOLUME")

        print(session.volume)

        # =====================================================
        # MULTI TIMEFRAME
        # =====================================================

        self.section("MULTI TIMEFRAME")

        if session.mtf:

            for tf, info in session.mtf.items():

                direction = (
                    "Bullish"
                    if info["bullish"]
                    else "Bearish"
                )

                print(f"{tf:<5} : {direction}")

        else:

            print("No MTF analysis")

        # =====================================================
        # CONFLUENCE
        # =====================================================

        self.section("CONFLUENCE")

        print(session.confluence)

        # =====================================================
        # VALIDATION
        # =====================================================

        self.section("VALIDATION")

        print(session.validation)

        # =====================================================
        # CHECKLIST
        # =====================================================

        self.section("CHECKLIST")

        print(session.checklist)

        # =====================================================
        # DECISION
        # =====================================================

        self.section("DECISION")

        print(session.decision)

        # =====================================================
        # AI
        # =====================================================

        self.section("AI")

        print(session.ai)

        # =====================================================
        # REPORT
        # =====================================================

        self.section("REPORT")

        print(session.report)

        print(self.LINE)
        print("END OF SESSION")
        print(self.LINE)

    def section(self, title):

        print()
        print(self.SEP)
        print(title)
        print(self.SEP)