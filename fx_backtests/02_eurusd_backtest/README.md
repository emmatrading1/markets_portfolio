# EUR/USD Backtest

Moving average crossover with volatility filtering, tested from January 2020 to October 2025.

---

## Results

| Metric | Strategy | Buy & Hold |
|--------|----------|------------|
| Return | +12.84% | +2.65% |
| Sharpe | 0.46 | - |
| Max Drawdown | -9.01% | ~-15% |
| Win Rate | 47.63% | - |
| Trades | 39 | - |

Strategy outperformed buy-and-hold by exiting before the 2022 EUR crisis. While buy-and-hold dropped 15%, the strategy stayed flat, then re-entered for the 2023-2024 recovery.

![Equity Curve](results/eurusd_backtest_equity.png)

---

## Strategy

- **Entry:** 20-day MA crosses above 50-day MA, ATR above 30th percentile
- **Exit:** 20-day MA crosses below 50-day MA

---

## Files

- `download_data.py` — fetches data from Yahoo Finance
- `strategy.py` — backtest implementation
- `results/` — equity curve and output

---

## Limitations

No transaction costs, assumes execution at close, no slippage. Real performance would be lower.
