from app.validation.trade_validator import validate_trade
# from app.analysis.validation.trade_validator import validate_trade


class ValidationStage:

    def run(self, session):
        
        def run(self, session):

            print("Running Validation Stage")

    # ------------------------------------
    # No trade to validate
    # ------------------------------------

        if (
            not hasattr(session, "trade")
            or not session.trade
            or "risk_reward" not in session.trade
        ):

            session.validation = {

            "valid": False,

            "confidence": 0,

            "score": 0,

            "reasons": ["No trade generated"],

            "warnings": []

        }

        return session

    # Existing validation code continues...

        print("Running Validation Stage")

        validation = validate_trade(
            trade=session.trade,
            smart_money=session.smart_money,
            structure=session.structure,
            volume=session.volume,
            indicators=session.indicators
        )

        session.validation.update(validation)

        return session