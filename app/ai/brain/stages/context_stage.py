class ContextStage:

    def process(self, context):

        if context:

            return {

                "valid": True,

                "message": context

            }

        return {

            "valid": False,

            "message": "No historical context"

        }