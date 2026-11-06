# FX Systematic Backtests

Python backtests of trend-following strategies on major FX pairs.

The goal is to test whether basic momentum signals (moving average crossovers) combined with a volatility filter can produce a stable performance across currencies.

Pairs tested:
- USD/JPY
- EUR/USD
- and GBP/USD

The strategy uses a 20 / 50 moving average crossover and only trades when volatility (ATR) is above a threshold to avoid to avoid periods when the market goes up and down without a clear direction.

Each folder contains the data download, the strategy logic, and the backtest results.

## Results (Jan 2020 – Oct 2025)

| Pair | Strategy | Buy & hold | Sharpe | Max drawdown | Details |
|---|---|---|---|---|---|
| USD/JPY | +24.5% | +45.6% | 0.64 | −9.4% | [open](./01_usdjpy_backtest) |
| EUR/USD | +12.8% | +2.7% | 0.46 | −9.0% | [open](./02_eurusd_backtest) |
| GBP/USD | +18.7% | +2.8% | 0.61 | −5.1% | [open](./03_gbpusd_backtest) |

The backtest ignores trading fees and assumes every trade is made at the exact price, so real results would actually be a bit lower.