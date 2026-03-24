# GBP/USD Backtest

Moving average crossover with volatility filtering, tested from January 2020 to October 2025.

---

## Results

| Metric | Strategy | Buy & Hold |
|--------|----------|------------|
| Return | +18.70% | +2.83% |
| Sharpe | 0.61 | - |
| Max Drawdown | -5.09% | ~-18% |
| Win Rate | 53.38% | - |
| Trades | 37 | - |

Best risk-adjusted performance of the three pairs. The strategy exited before Cable's 2022 crash from 1.40 to 1.05, then captured the 2023-2025 recovery. Lowest drawdown despite GBP being the most volatile pair.

![Equity Curve](results/gbpusd_backtest_equity.png)

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
