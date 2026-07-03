from app.validation.trade_validator import validate_trade


class ValidationStage:

    def run(self, session):

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