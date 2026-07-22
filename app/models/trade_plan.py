from dataclasses import dataclass


@dataclass
class TradePlan:
    """
    Complete trading plan produced by the analysis pipeline.
    """

    entry: float | None = None

    stop_loss: float | None = None

    take_profit: float | None = None

    risk_reward: float = 0.0

    position_size: float | None = None

    risk_amount: float | None = None

    direction: str = ""

    strategy: str = ""

    confidence: float = 0.0

    valid: bool = False