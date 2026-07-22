from app.ai.brain.stages.context_stage import ContextStage
from app.ai.brain.stages.strategy_stage import StrategyStage
from app.ai.brain.stages.confidence_stage import ConfidenceStage
from app.ai.brain.stages.risk_stage import RiskStage
from app.ai.brain.stages.execution_stage import ExecutionStage


class DecisionBrain:
    """
    Central AI reasoning engine.
    """

    def __init__(self):

        self.context = ContextStage()

        self.strategy = StrategyStage()

        self.confidence = ConfidenceStage()

        self.risk = RiskStage()

        self.execution = ExecutionStage()

    def think(

        self,

        strategy,

        context,

        confidence,

        risk

    ):

        context_result = self.context.process(
            context
        )

        strategy_result = self.strategy.process(
            strategy
        )

        confidence_result = self.confidence.process(
            confidence
        )

        risk_result = self.risk.process(
            risk
        )

        execution_result = self.execution.process(

            strategy_result,

            context_result,

            confidence_result,

            risk_result

        )

        return {

            "strategy": strategy_result["strategy"],

            "context": context_result["message"],

            "confidence": confidence_result["confidence"],

            "risk": risk_result["risk"],

            "execute": execution_result["execute"],

            "reason": [

                context_result["message"],

                f"Confidence: {confidence_result['confidence']}",

                f"Risk: {risk_result['risk']}%"

            ]

        }