from dataclasses import dataclass, field


@dataclass
class TradingSession:

    symbol: str = ""

    indicators: dict = field(default_factory=dict)

    structure: dict = field(default_factory=dict)

    smart_money: dict = field(default_factory=dict)

    confluence: dict = field(default_factory=dict)

    decision: dict = field(default_factory=dict)

    validation: dict = field(default_factory=dict)

    checklist: dict = field(default_factory=dict)

    ai_context: dict = field(default_factory=dict)

    reports: list = field(default_factory=list)