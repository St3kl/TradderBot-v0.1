from dataclasses import dataclass


@dataclass
class TradeMemory:

    symbol: str

    strategy: str

    direction: str

    entry: float

    stop_loss: float

    take_profit: float

    risk_reward: float

    confidence: float

    trend: str

    phase: str

    confluence: float

    volume_score: float

    smart_money: dict

    result: str = ""

    profit: float = 0