class ExecutionValidator:

    def validate(self, session):

        decision = session.decision

        if decision["action"] == "WAIT":

            return False

        if session.trade_plan.entry is None:

            return False

        if session.trade_plan.position_size is None:

            return False

        if session.trade_plan.risk_reward < 2:

            return False

        return True