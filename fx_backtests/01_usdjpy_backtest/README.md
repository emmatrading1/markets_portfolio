# USD/JPY Backtest

Moving average crossover with volatility filtering, tested from January 2020 to October 2025.

---

## Results

| Metric | Strategy | Buy & Hold |
|--------|----------|------------|
| Return | +24.45% | +45.59% |
| Sharpe | 0.64 | - |
| Max Drawdown | -9.44% | ~-20% |
| Win Rate | 54.74% | - |
| Trades | 33 | - |

Lower returns than buy-and-hold, but half the drawdown. The strategy was out of the market during JPY's sharp 2024-2025 move—missed upside, but preserved capital during volatile periods.

![Equity Curve](results/usdjpy_backtest_equity.png)

---

## Strategy

- **Entry:** 20-day MA crosses above 50-day MA, ATR above 30th percentile
- **Exit:** 20-day MA crosses below 50-day MA

The volatility filter avoids whipsaw trades during low-vol consolidation.

---

## Files

- `download_data.py` — fetches data from Yahoo Finance
- `strategy.py` — backtest implementation
- `results/` — equity curve and output

---

## Limitations

No transaction costs, assumes execution at close, no slippage. Real performance would be lower.
