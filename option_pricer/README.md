###Option Pricer

Small Python tool to price European options using the Black-Scholes model.

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

I wanted a simple tool to experiment with option pricing instead of only working with formulas. It helps me how markets think about sensitivities, hedging, and volatility.

Features

Prices European calls and puts  
Computes Greeks  
Checks put-call parity  
Runs spot and volatility sensitivity tests  
Estimates implied volatility  
Shows delta hedge intuition  
Plots option profit at expiry