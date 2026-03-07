# Option Pricer

Small Python project where I implemented a basic Black-Scholes option pricer.

The goal was mainly to build intuition around how option prices react to volatility, time to maturity, interest rates and moneyness.

Right now the tool prices European calls and puts and includes a quick put-call parity check.

Files:

black_scholes.py  
Core pricing functions.

pricer_app.py  
Simple script where I run the pricer with example parameters.

greeks.py  
Work in progress — adding delta, gamma, vega and theta.

Why I built it:

I wanted a simple tool to experiment with option pricing instead of just using formulas from class. It also helps understand how traders think about volatility and sensitivities.

Next steps:

- add Greeks  
- add volatility sensitivity tests  
- plot payoff profiles  
- eventually turn it into a small interactive pricer