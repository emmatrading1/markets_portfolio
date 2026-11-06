# Macro Event Tracker

This project tracks how major markets react to key macroeconomic events.

The idea is the following : after important releases (CPI, NFP, central bank decisions, etc.), I record how different assets move in the minutes and hours following the announcement.

Assets I track include:

- FX (EUR/USD, USD/JPY)
- Rates (US 10Y yields)
- Equities (S&P 500 futures)
- and Commodities (gold, oil)

Over time this should create a small dataset of event reactions that can be used to spot patterns in market behaviour.

## Example: FOMC decision, March 19, 2026

| Asset | Move |
|---|---|
| US 2Y yield | +15bp |
| DXY | +0.60% |
| S&P 500 | −1.10% |
| Gold | −0.80% |

When the Fed sounds tougher than expected, short-term rates rise first, then the dollar goes up and stocks and gold fall.

## Files

- `data/events_log.csv`: every event with forecast, actual, asset move and my comment
- `scripts/event_utils.py`: functions to compute surprises, reactions by asset and the biggest shocks
- `notebooks/event_analysis.ipynb`: the analysis (open it on GitHub to see the tables)
