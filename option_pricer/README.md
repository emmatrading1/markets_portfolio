# Option Pricer

Simple Python implementation of a Black-Scholes option pricer built to explore option valuation and sensitivities in equity derivatives.

## What it does

- prices European call and put options
- takes standard Black-Scholes inputs:
  - spot price
  - strike
  - maturity
  - interest rate
  - volatility
- includes a basic put-call parity check

## Files

- `black_scholes.py` — pricing functions
- `pricer_app.py` — example run and diagnostics
- `greeks.py` — Greeks calculations (building)

## Example inputs

- Spot: 100
- Strike: 100
- Maturity: 1 year
- Rate: 5%
- Volatility: 20%

## Example output

- Call price: ~10.45
- Put price: ~5.57

## Why I built it

I wanted a clean tool to understand how option prices react to volatility, rates, time to maturity and moneyness, and to build intuition that is useful for derivatives and structuring roles.

## Next steps

- add Greeks
- add volatility sensitivity analysis
- add payoff charts
- turn it into a simple interactive pricer