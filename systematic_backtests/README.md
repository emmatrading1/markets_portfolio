### FX Systematic Backtests

Simple Python backtests of trend-following strategies on major FX pairs.

The goal is to test whether basic momentum signals (moving average crossovers) combined with a volatility filter can produce stable performance across currencies.

Pairs tested:
- USD/JPY
- EUR/USD
- GBP/USD

The strategy uses a 20 / 50 moving average crossover and only trades when volatility (ATR) is above a threshold to avoid choppy markets.

Each folder contains the data download, the strategy logic, and the backtest results.

This is mainly an exploration project to understand how systematic FX strategies behave across different pairs.