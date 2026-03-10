## Option Pricer

Small Python tool to price European options using the Black-Scholes model.

The project was built to develop intuition about how option prices react to changes in volatility, time to maturity, interest rates, and moneyness.

The tool currently prices European calls and puts, computes the main option Greeks, performs simple sensitivity tests, and visualizes option payoff profiles.


Files

black_scholes.py  
Core pricing functions implementing the Black-Scholes model.

greeks.py  
Computation of option sensitivities (delta, gamma, vega, theta).

pricer_app.py  
Main script used to run the pricer with user inputs, display diagnostics, and generate payoff visualizations.


Why I built it

I wanted a simple tool to experiment with option pricing instead of only working with formulas.  
Building the model helped me better understand how traders think about option valuation, sensitivities, and risk.


Features

Prices European call and put options  
Computes option Greeks (delta, gamma, vega, theta)  
Performs spot and volatility sensitivity tests  
Checks put-call parity  
Plots option profit at expiry


Next steps

- Add implied volatility calculation  
- Add interactive inputs and scenario testing  
- Extend payoff visualization to multi-option strategies