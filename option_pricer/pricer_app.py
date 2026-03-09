from black_scholes import black_scholes_call, black_scholes_put
import math

# Example parameters
S = 100      # spot
K = 100      # strike
T = 1.0      # maturity in years
r = 0.05     # risk-free rate
sigma = 0.20 # volatility

call_price = black_scholes_call(S, K, T, r, sigma)
put_price = black_scholes_put(S, K, T, r, sigma)

forward = S * math.exp(r * T)
discounted_strike = K * math.exp(-r * T)
parity_lhs = call_price - put_price
parity_rhs = S - discounted_strike

print("=== Black-Scholes Option Pricer ===")

S = float(input("Spot price (S): "))
K = float(input("Strike (K): "))
T = float(input("Maturity in years (T): "))
r = float(input("Risk-free rate (r): "))
sigma = float(input("Volatility (sigma): "))

print(f"Call price: {call_price:.4f}")
print(f"Put price:  {put_price:.4f}")
print()

print("=== Diagnostics ===")
print(f"Forward price estimate: {forward:.4f}")
print(f"Call - Put:            {parity_lhs:.4f}")
print(f"S - K*e^(-rT):         {parity_rhs:.4f}")
print(f"Parity difference:     {abs(parity_lhs - parity_rhs):.8f}")

if S > K:
    print("Moneyness: in-the-money call / out-of-the-money put")
elif S < K:
    print("Moneyness: out-of-the-money call / in-the-money put")
else:
    print("Moneyness: at-the-money")

    import math
from black_scholes import black_scholes_call, black_scholes_put
from greeks import (
    call_delta,
    put_delta,
    gamma,
    vega,
    call_theta,
    put_theta,
)

# Example inputs
S = 100
K = 100
T = 1.0
r = 0.05
sigma = 0.20

call_price = black_scholes_call(S, K, T, r, sigma)
put_price = black_scholes_put(S, K, T, r, sigma)

c_delta = call_delta(S, K, T, r, sigma)
p_delta = put_delta(S, K, T, r, sigma)
opt_gamma = gamma(S, K, T, r, sigma)
opt_vega = vega(S, K, T, r, sigma)
c_theta = call_theta(S, K, T, r, sigma)
p_theta = put_theta(S, K, T, r, sigma)

parity_lhs = call_price - put_price
parity_rhs = S - K * math.exp(-r * T)

print("=== Black-Scholes Option Pricer ===")
print(f"Spot: {S}")
print(f"Strike: {K}")
print(f"Maturity: {T}")
print(f"Rate: {r}")
print(f"Volatility: {sigma}")
print()

print("=== Prices ===")
print(f"Call: {call_price:.4f}")
print(f"Put:  {put_price:.4f}")
print()

print("=== Greeks ===")
print(f"Call Delta: {c_delta:.4f}")
print(f"Put Delta:  {p_delta:.4f}")
print(f"Gamma:      {opt_gamma:.6f}")
print(f"Vega:       {opt_vega:.4f}")
print(f"Call Theta: {c_theta:.4f}")
print(f"Put Theta:  {p_theta:.4f}")
print()

print("=== Parity Check ===")
print(f"Call - Put:        {parity_lhs:.4f}")
print(f"S - K*e^(-rT):     {parity_rhs:.4f}")
print(f"Difference:        {abs(parity_lhs - parity_rhs):.8f}")

print("\n=== Volatility Sensitivity ===")

for vol in [0.10, 0.15, 0.20, 0.25, 0.30]:
    price = black_scholes_call(S, K, T, r, vol)
    print(f"Vol {vol:.2f} -> Call Price {price:.4f}")