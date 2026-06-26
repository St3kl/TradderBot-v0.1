# TradderBot - Project Brain

**Version:** 0.1.0
**Status:** Active Development
**Last Updated:** June 2026

---

# 1. Project Overview

## Purpose

TradderBot is an AI-assisted trading analysis platform designed to help traders identify high-quality trading opportunities across multiple financial markets.

The project is **not** intended to blindly generate buy or sell signals.

Instead, it combines deterministic market analysis with AI-powered reasoning to produce explainable, consistent, and backtestable trade recommendations.

The current version begins as a Telegram bot, but this is only the first stage of a much larger platform.

---

# 2. Long-Term Vision

The final objective is to build an institutional-grade trading intelligence platform capable of analyzing multiple markets, detecting opportunities, ranking trades, and explaining every decision.

Supported markets will eventually include:

* Cryptocurrency
* Forex
* Stocks
* Commodities
* Indices
* Futures

The final platform should include:

* AI-assisted market analysis
* Multi-timeframe analysis
* Pattern recognition
* Market structure detection
* Confluence engine
* Risk management
* Trade grading
* Opportunity scanner
* Portfolio monitoring
* Broker integrations
* Web dashboard
* Historical database
* Backtesting engine
* Machine Learning enhancements

---

# 3. Core Philosophy

## AI is NOT the trader.

AI is the analyst.

Trading decisions must come from deterministic algorithms that can be tested and verified.

AI is responsible for:

* Explaining signals
* Summarizing market conditions
* Highlighting risks
* Assisting the user

AI is NOT responsible for:

* Inventing buy signals
* Guessing entries
* Guessing stop losses
* Guessing take profits

---

# 4. Design Principles

Every module should satisfy the following principles:

### Modular

Every feature belongs in its own module.

### Explainable

Every decision must be explainable.

### Deterministic

The same inputs should always produce the same outputs.

### Testable

Every module should be independently testable.

### Replaceable

Any module should be replaceable without affecting the rest of the system.

---

# 5. High-Level Architecture

```
Market APIs
      │
      ▼
Market Layer
      │
      ▼
Indicator Engine
      │
      ▼
Pattern Detection
      │
      ▼
Market Structure
      │
      ▼
Support & Resistance
      │
      ▼
Risk Engine
      │
      ▼
Confluence Engine
      │
      ▼
Scoring Engine
      │
      ▼
Decision Engine
      │
      ▼
AI Explanation Layer
      │
      ▼
Telegram Bot
      │
      ▼
Web Dashboard
```

---

# 6. Current Technology Stack

## Language

Python 3.11

---

## Current Libraries

* python-telegram-bot
* pandas
* ta
* requests

Future:

* FastAPI
* PostgreSQL
* Redis
* Celery
* Docker
* React / Next.js

---

# 7. Current APIs

## Crypto

Binance API

Used for:

* Candles
* OHLC
* Volume
* Price

---

## Forex

TwelveData API

Current limitations:

* Free plan
* Limited requests
* ATR support incomplete
* Volume unavailable

---

# 8. Current Folder Structure

```
app/

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
│   ├── forex_client.py
│   └── forex_indicators.py
│
├── patterns/
│   ├── detector.py
│   └── support_resistance.py
│
├── risk/
│   ├── atr.py
│   └── calculator.py
│
└── ai/
```

---

# 9. Current Features

## Crypto

Completed

* Binance Market Data
* EMA 50
* EMA 200
* RSI
* ATR
* Volume
* Multi-Timeframe
* Pattern Detection
* Support
* Resistance
* Entry
* Stop Loss
* Take Profit
* Risk Reward
* Trade Score
* Trade Grade

---

## Forex

Completed

* Price
* EMA50
* EMA200
* RSI
* Support
* Resistance
* Entry
* Stop Loss
* Take Profit

Pending

* ATR
* Volume
* Multi-Timeframe

---

# 10. Telegram Commands

Current:

```
/analyze BTCUSDT

/analyze ETHUSDT

/analyze EURUSD
```

Output includes:

* Trend
* Pattern
* Support
* Resistance
* Entry
* Stop Loss
* Take Profit
* Risk Reward
* ATR
* Volume
* Confidence
* Trade Score
* Grade

---

# 11. Current Scoring System

Maximum Score: 100

Trend

25

RSI

20

Volume

20

Multi-Timeframe

25

Pattern

10

Grades

95+

A+ Elite

90+

A+

85+

A

75+

B

65+

C

Below 65

Avoid

---

# 12. Current Trading Logic

Trend

EMA50 > EMA200

Bullish

EMA50 < EMA200

Bearish

Risk Reward

1 : 2

Entry

Current Market Price

Stop Loss

Nearest Support (Long)

Nearest Resistance (Short)

Take Profit

Risk × 2

---

# 13. Completed Development Milestones

✓ Telegram Bot

✓ Binance Integration

✓ Forex Integration

✓ EMA

✓ RSI

✓ ATR

✓ Volume

✓ Pattern Detection

✓ Support & Resistance

✓ Risk Calculator

✓ Multi-Timeframe Analysis

✓ Confidence Calculation

✓ Trade Grading

✓ Scoring Engine

---

# 14. Known Limitations

Forex ATR is incomplete because the current API does not consistently provide high and low values.

Forex Volume is unavailable on the free API.

AI integration is disabled until deterministic analysis is mature.

The scoring engine is intentionally simple and will evolve as more analysis modules are added.

---

# 15. Common Errors Encountered

During development, several recurring issues were solved:

* ModuleNotFoundError due to missing project modules.
* OpenAI API quota errors when no API key or quota was available.
* IndentationError caused by misplaced code blocks.
* SyntaxError: await outside function caused by moving code outside the async handler.
* NameError for variables such as `bullish`, `trade`, `highs`, and `volume_score`.
* KeyError for missing dictionary keys such as `closes`, `atr`, and `values`.
* Telegram Conflict caused by running more than one polling instance.
* Forex API limitations resulting in missing data fields.

Future contributors should consult the Development Log before debugging similar issues.

---

# 16. Future Roadmap

Phase 2

* Trend Strength
* Market Structure
* Confluence Engine
* Trade Filter

Phase 3

* Market Scanner
* Opportunity Ranking
* Historical Database
* Backtesting

Phase 4

* AI Explanation Layer
* News Sentiment
* Machine Learning

Phase 5

* Dashboard
* Broker Integration
* Portfolio Tracking
* SaaS Platform

---

# 17. Development Rules

Every new feature must:

* Have its own module.
* Be documented.
* Be independently testable.
* Improve the scoring engine or decision quality.
* Preserve backward compatibility whenever possible.

Avoid placing business logic directly inside `telegram_bot.py`. The bot should orchestrate modules rather than implement analysis itself.

---

# 18. AI Collaboration Rules

When using ChatGPT, Claude, Gemini, Kimi, or any other AI:

* Do not redesign the architecture without a strong reason.
* Extend existing modules instead of rewriting them.
* Prefer deterministic algorithms over AI-generated decisions.
* Explain the reasoning behind any architectural change.
* Preserve modularity and readability.
* Keep documentation synchronized with code changes.

---

# 19. Ultimate Objective

The Telegram bot is only Version 0.1.

The real goal is to build a complete AI-assisted trading operating system capable of analyzing markets, ranking opportunities, managing risk, explaining every recommendation, and eventually serving as a professional trading intelligence platform for advanced retail traders and small trading firms.

Every module developed today should contribute toward that long-term vision.
