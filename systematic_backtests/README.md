# FX Systematic Backtests

Moving average crossover strategies with volatility filtering, tested across USD/JPY, EUR/USD, and GBP/USD from January 2020 to October 2025.

---

## Results

| Pair | Strategy Return | Buy & Hold | Sharpe | Max Drawdown | Trades |
|------|----------------|------------|--------|--------------|--------|
| USD/JPY | +24.45% | +45.59% | 0.64 | -9.44% | 33 |
| EUR/USD | +12.84% | +2.65% | 0.46 | -9.01% | 39 |
| GBP/USD | +18.70% | +2.83% | 0.61 | -5.09% | 37 |

EUR/USD and GBP/USD significantly outperformed buy-and-hold. USD/JPY underperformed on raw returns but with half the drawdown.

---

## Strategy Logic

- **Entry:** 20-day MA crosses above 50-day MA, volatility (ATR) above 30th percentile
- **Exit:** 20-day MA crosses below 50-day MA

The volatility filter keeps the strategy out of choppy, range-bound markets.

---

## Repository Structure
```
projects/
├── 01_usdjpy_backtest/
├── 02_eurusd_backtest/
└── 03_gbpusd_backtest/
```

Each folder contains `download_data.py`, `strategy.py`, and results.

---

## Limitations

Backtests assume perfect execution at close prices, no transaction costs, no slippage. Real-world performance would be lower.

---

*Past performance does not guarantee future results.*
