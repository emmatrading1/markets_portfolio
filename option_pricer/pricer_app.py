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
print(f"Spot (S): {S}")
print(f"Strike (K): {K}")
print(f"Maturity (T): {T}")
print(f"Rate (r): {r}")
print(f"Volatility (sigma): {sigma}")
print()

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