class ExecutionFactory:
    """
    Creates execution results.
    """

    @staticmethod
    def create(**overrides):

        execution = {

            "execute": True,

            "reason": "Test",

            "risk": {

                "position": {

                    "position_size": 0.25,

                    "risk_amount": 100

                }

            }

        }

        execution.update(overrides)

        return execution