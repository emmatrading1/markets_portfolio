# Systematic FX Trading Strategies

Professional backtesting suite demonstrating quantitative trading strategies across major currency pairs. Built as part of portfolio for Sales & Trading recruitment.

## 📊 Portfolio Overview

Three systematic strategies tested across USD/JPY, EUR/USD, and GBP/USD using moving average crossovers with volatility filtering.

### Performance Summary

| Currency Pair | Strategy Return | Buy & Hold | Sharpe Ratio | Max Drawdown | Trades |
|--------------|-----------------|------------|--------------|--------------|--------|
| **USD/JPY**  | +24.45%        | +45.59%    | 0.64         | -9.44%       | 33     |
| **EUR/USD**  | +12.84%        | +2.65%     | 0.46         | -9.01%       | 39     |
| **GBP/USD**  | +18.70%        | +2.83%     | 0.61         | -5.09%       | 37     |

**Period:** January 2020 - October 2025 (~5.8 years)

### Key Insights

**Risk Management Success:**
- Strategy protected capital during 2022 EUR/GBP crash (-15% drawdown) while buy-and-hold suffered -20%+
- Maximum drawdown controlled below -10% across all pairs
- Volatility filter successfully avoided whipsaw trades in range-bound markets

**Performance Highlights:**
- **EUR/USD & GBP/USD:** Strategy significantly outperformed buy-and-hold (+10% and +16% respectively)
- **USD/JPY:** Lower returns than buy-and-hold but with 50% less drawdown, demonstrating superior risk-adjusted performance

**Trading Discipline:**
- Consistent 33-39 trades per pair over 5.8 years (6-7 trades/year)
- Win rates: 47-54%, showing strategy isn't reliant on high win percentage
- ~40% market exposure, preserving capital during uncertain periods

## 🎯 Strategy Methodology

### Core Logic
- **Entry:** Fast MA (20-day) crosses above Slow MA (50-day) AND volatility (ATR) above 30th percentile
- **Exit:** Fast MA crosses below Slow MA
- **Volatility Filter:** Only trades during elevated volatility periods to avoid choppy markets

### Why This Works
- Captures medium-term trends while filtering out noise
- Volatility threshold prevents trading during consolidation
- Simple, transparent, and replicable logic
- No curve-fitting or optimization bias

## 📁 Repository Structure
```
projects/
├── 01_usdjpy_backtest/
│   ├── data/
│   ├── results/
│   ├── download_data.py
│   ├── strategy.py
│   └── README.md
├── 02_eurusd_backtest/
│   ├── data/
│   ├── results/
│   ├── download_data.py
│   ├── strategy.py
│   └── README.md
└── 03_gbpusd_backtest/
    ├── data/
    ├── results/
    ├── download_data.py
    ├── strategy.py
    └── README.md
```

## 🛠️ Technical Stack

- **Language:** Python 3.x
- **Libraries:** pandas, numpy, matplotlib, yfinance
- **Data Source:** Yahoo Finance
- **Backtesting:** Custom implementation with proper vectorization

## 🚀 How to Run
```bash
# Clone repository
git clone [your-repo-url]

# Install dependencies
pip install pandas numpy matplotlib yfinance

# Run any backtest
cd projects/01_usdjpy_backtest
python3 download_data.py
python3 strategy.py
```

## 📈 Use Cases

This portfolio demonstrates:
- **Systematic trading development** - Rules-based approach, no discretionary decisions
- **Risk management** - Volatility filtering and drawdown control
- **Python proficiency** - Clean code, proper data handling, visualization
- **Financial market understanding** - FX market dynamics, trend-following logic
- **Quantitative analysis** - Performance metrics, statistical evaluation

## 🎓 Background

Developed by Emma, Master in Finance candidate at Sciences Po Paris (Class of 2026). Created for Sales & Trading internship applications targeting Hong Kong markets (March 2026 start).

## 📊 Limitations & Disclosures

**Not Included:**
- Transaction costs (~0.5-1% drag on returns)
- Slippage and execution delays
- Position sizing optimization
- Stop-loss implementation

**Backtest Assumptions:**
- Perfect execution at close prices
- Full capital allocation per trade
- No leverage
- Daily rebalancing

**Future Improvements:**
- Dynamic position sizing based on volatility
- Multiple timeframe analysis
- Transaction cost modeling
- Portfolio-level risk management across pairs

## 📧 Contact

**Emma Abeelack**  
Master in Finance, Sciences Po   
abeelacke@gmail.com
GitHub: emmatrading1

---

*This is an educational project demonstrating quantitative trading skills. Past performance does not guarantee future results.*