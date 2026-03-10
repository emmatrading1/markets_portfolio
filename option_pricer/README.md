## Option Pricer

Small Python tool to price European options with the Black-Scholes model.

It prices calls and puts, computes the main Greeks, checks put-call parity, runs simple spot and volatility tests, estimates implied volatility, and plots profit at expiry.

Files

black_scholes.py  
Core pricing functions.

greeks.py  
Delta, gamma, vega, theta.

implied_vol.py  
Implied volatility solver.

pricer_app.py  
Interactive script to run the pricer, diagnostics, sensitivity tests, and plot.

Why I built it

I wanted a simple project to make option pricing more concrete and to better understand how traders think about sensitivities, hedging, and volatility.

Main features

Prices European calls and puts  
Computes Greeks  
Checks put-call parity  
Runs spot and volatility sensitivity tests  
Estimates implied volatility  
Shows delta hedge intuition  
Plots option profit at expiry