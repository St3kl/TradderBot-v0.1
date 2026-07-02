from app.validation.trade_validator import validate_trade



class ValidationStage:

    def run(self, session):

        print("Running Validation Stage")
        print("VALIDATION RECEIVED:", session.trade)

        session.validation = validate_trade(
            trade=session.trade,
            smart_money=session.smart_money,
            structure=session.structure,
            volume=session.volume,
            indicators=session.indicators
        )
        print(session.trade)

        return session
    
    