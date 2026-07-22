from dataclasses import dataclass
from datetime import datetime


@dataclass
class TradeExecuted:

    # ----------------------------------
    # Trade
    # ----------------------------------

    symbol: str
    side: str

    entry: float
    stop_loss: float
    take_profit: float

    # ----------------------------------
    # AI Decision
    # ----------------------------------

    confidence: int

    # ----------------------------------
    # Trading Context
    # ----------------------------------

    strategy: str
    regime: str
    volatility: str

    # ----------------------------------
    # Metadata
    # ----------------------------------

    timestamp: datetime


@dataclass
class TradeClosed:

    symbol: str
    pnl: float
    duration: float
    timestamp: datetime


@dataclass
class BacktestFinished:

    trades: int
    win_rate: float
    pnl: float
    timestamp: datetime