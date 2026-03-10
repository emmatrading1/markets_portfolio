<p style="font-size:22px; font-weight:600;">Option Pricer</p>

Small Python tool to price European options using the Black-Scholes model.

The project prices European calls and puts, computes option Greeks, checks put-call parity, runs spot and volatility sensitivity tests, estimates implied volatility, and visualizes profit at expiry.

Files

black_scholes.py  
Core Black-Scholes pricing functions.

greeks.py  
Computation of option sensitivities (delta, gamma, vega, theta).

implied_vol.py  
Implied volatility solver using Newton’s method.

pricer_app.py  
Main script that runs the pricer, diagnostics, sensitivity tests, and payoff visualization.

Why I built it

I wanted a simple tool to experiment with option pricing rather than only working with formulas from class. Building it helped me better understand how traders think about sensitivities, volatility and hedging.

Features

Prices European calls and puts  
Computes Greeks (delta, gamma, vega, theta)  
Checks put-call parity  
Runs spot and volatility sensitivity tests  
Estimates implied volatility  
Shows delta-hedging intuition  
Plots option profit at expiry