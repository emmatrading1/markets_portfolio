### Option Pricer

Python tool to price and analyze European options using Black-Scholes.

The project prices calls and puts, computes Greeks, checks put-call parity, runs spot and volatility sensitivity tests, estimates implied volatility, and plots profit at expiry.

Files

black_scholes.py
Core pricing functions implementing the Black-Scholes model.

greeks.py
Computation of option sensitivities (delta, gamma, vega, theta).

implied_vol.py
Implied volatility solver using Newton’s method.

pricer_app.py
Main script to run the pricer, diagnostics, sensitivity tests, and payoff visualization.

Why I built it

Built to better understand pricing, sensitivities, and hedging mechanics in practice.

Features

Prices European calls and puts  
Computes Greeks  
Checks put-call parity  
Runs spot and volatility sensitivity tests  
Estimates implied volatility  
Shows delta hedge intuition  
Plots option profit at expiry