from dataclasses import dataclass
from typing import List


@dataclass
class SwingPoint:
    index: int
    price: float
    kind: str  # HIGH or LOW


@dataclass
class StructureResult:

    trend: str

    phase: str

    bullish_bos: bool

    bearish_bos: bool

    bullish_choch: bool

    bearish_choch: bool

    swing_highs: List[SwingPoint]

    swing_lows: List[SwingPoint]

    confidence: int