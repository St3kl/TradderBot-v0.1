# 04_ARCHITECTURE.md

# TradderBot Architecture

Version: v0.1 (Refactored)

---

# High-Level Architecture

```
                    Telegram User
                         │
                         ▼
                telegram_bot.py
                         │
                         ▼
              services/analysis_service.py
                         │
 ┌───────────────────────┼────────────────────────┐
 ▼                       ▼                        ▼
Market Layer         Analysis Layer          Report Layer
 │                       │                        │
 ▼                       ▼                        ▼
Crypto              Multi-Timeframe        report_builder.py
Forex               Pattern Detection
Indicators          Volume Analysis
                    Trend Analysis
                    Signal Scoring
                    Risk Management
```

The Telegram bot is now only responsible for receiving commands and sending responses.

All trading logic has been moved into reusable services.

---

# Project Structure

```
TradderBot_v01/

app/

├── ai/
│
├── analysis/
│   ├── multi_timeframe.py
│   ├── scoring.py
│   └── volume.py
│
├── bot/
│   └── telegram_bot.py
│
├── market/
│   ├── indicators.py
│   ├── forex_indicators.py
│   └── forex_client.py
│
├── patterns/
│   ├── detector.py
│   └── support_resistance.py
│
├── reports/
│   └── report_builder.py
│
├── risk/
│   ├── atr.py
│   └── calculator.py
│
├── services/
│   └── analysis_service.py
│
└── main.py
```

---

# Current Data Flow

```
Telegram Command

        │

        ▼

telegram_bot.py

        │

        ▼

analysis_service.py

        │

        ├── Detect Asset Type
        │
        ├── Crypto
        │      │
        │      └── Binance Indicators
        │
        └── Forex
               │
               └── Forex Indicators

        ▼

Pattern Detection

        ▼

Volume Analysis

        ▼

Support / Resistance

        ▼

ATR

        ▼

Trade Levels

        ▼

Multi-Timeframe Analysis

        ▼

Signal Scoring

        ▼

Report Builder

        ▼

Telegram Reply
```

---

# Responsibilities

## telegram_bot.py

Responsible only for:

* Telegram commands
* User input
* Calling the Analysis Service
* Sending the report

It contains no trading logic.

---

## analysis_service.py

The central brain of TradderBot.

Responsibilities:

* Detect market type
* Load indicators
* Detect chart patterns
* Analyze volume
* Calculate support/resistance
* Calculate ATR
* Calculate trade levels
* Perform multi-timeframe analysis
* Calculate signal score
* Generate the final report

Every future interface (Telegram, Web API, Dashboard, Scanner) should use this service.

---

## report_builder.py

Responsible only for presentation.

It converts analysis results into a formatted Telegram report.

No calculations are performed here.

---

## market/

Provides raw market data.

Current providers:

* Binance (Crypto)
* Forex API

Future:

* Bybit
* OANDA
* MetaTrader 5
* Interactive Brokers

---

## analysis/

Contains analytical algorithms.

Current modules:

* Multi-Timeframe Analysis
* Volume Analysis
* Signal Scoring

Future modules:

* Trend Strength
* Smart Money Concepts
* Liquidity Detection
* Market Structure
* Order Blocks
* Fair Value Gaps
* AI Confidence Engine

---

## patterns/

Responsible for technical pattern detection.

Current:

* Basic Pattern Detection
* Support / Resistance

Future:

* Head & Shoulders
* Double Tops
* Double Bottoms
* Triangles
* Flags
* Pennants
* Wedges
* Harmonic Patterns

---

## risk/

Responsible for trade management.

Current:

* ATR
* Entry
* Stop Loss
* Take Profit

Future:

* Dynamic Position Sizing
* Kelly Criterion
* Portfolio Risk
* Volatility Models

---

# Design Principles

The project follows:

* Single Responsibility Principle
* Modular Design
* Reusable Services
* Separation of Concerns
* Scalable Architecture

Each module should have one responsibility.

---

# Planned Architecture (v1.0)

```
Telegram
Web Dashboard
REST API
Scanner
Trading Bot
Desktop App

        │

        ▼

Analysis Service

        │

 ┌──────┼───────────┐
 ▼      ▼           ▼

Decision Engine

Market Engine

Risk Engine

AI Engine

Report Engine
```

Every component will reuse the same Analysis Service.

---

# Next Major Components

Priority order:

1. Decision Engine
2. Trend Strength Engine
3. Scanner Engine
4. AI Analysis Engine
5. Alert Engine
6. Backtesting Engine
7. Strategy Engine
8. Auto Trading Engine
9. Web Dashboard
10. Portfolio Manager

---

# Current Status

Completed:

* Crypto Analysis
* Forex Analysis
* EMA
* RSI
* ATR
* Multi-Timeframe Analysis
* Support / Resistance
* Trade Levels
* Volume Analysis
* Signal Scoring
* Report Builder
* Analysis Service Refactor

In Progress:

* Decision Engine

Future:

* AI Trading Assistant
* Portfolio Management
* Strategy Builder
* Automated Trading
* Web Platform
* Mobile Application
