import math
import matplotlib.pyplot as plt

from black_scholes import black_scholes_call, black_scholes_put
from greeks import (
    call_delta,
    put_delta,
    gamma,
    vega,
    call_theta,
    put_theta,
)


def call_profit_at_expiry(ST, K, premium):
    return max(ST - K, 0) - premium


def put_profit_at_expiry(ST, K, premium):
    return max(K - ST, 0) - premium


print("=== Black-Scholes Option Pricer ===")

option_type = input("Option type (call/put): ").strip().lower()
S = float(input("Spot price (S): "))
K = float(input("Strike (K): "))
T = float(input("Maturity in years (T): "))
r = float(input("Risk-free rate (r): "))
sigma = float(input("Volatility (sigma): "))

if option_type not in ["call", "put"]:
    raise ValueError("Option type must be 'call' or 'put'.")

if S <= 0 or K <= 0 or T <= 0 or sigma <= 0:
    raise ValueError("Spot, strike, maturity, and volatility must be positive.")

# Prices
call_price = black_scholes_call(S, K, T, r, sigma)
put_price = black_scholes_put(S, K, T, r, sigma)

# Greeks
c_delta = call_delta(S, K, T, r, sigma)
p_delta = put_delta(S, K, T, r, sigma)
opt_gamma = gamma(S, K, T, r, sigma)
opt_vega = vega(S, K, T, r, sigma)
c_theta = call_theta(S, K, T, r, sigma)
p_theta = put_theta(S, K, T, r, sigma)

# Parity diagnostics
forward = S * math.exp(r * T)
discounted_strike = K * math.exp(-r * T)
parity_lhs = call_price - put_price
parity_rhs = S - discounted_strike

# Moneyness
if S > K:
    moneyness = "in-the-money call / out-of-the-money put"
elif S < K:
    moneyness = "out-of-the-money call / in-the-money put"
else:
    moneyness = "at-the-money"

# Select chosen option
if option_type == "call":
    selected_price = call_price
    selected_delta = c_delta
    selected_theta = c_theta
    premium = call_price
else:
    selected_price = put_price
    selected_delta = p_delta
    selected_theta = p_theta
    premium = put_price

print("\n=== Inputs ===")
print(f"Option type: {option_type}")
print(f"Spot: {S}")
print(f"Strike: {K}")
print(f"Maturity: {T}")
print(f"Rate: {r}")
print(f"Volatility: {sigma}")
print(f"Moneyness: {moneyness}")

print("\n=== Prices ===")
print(f"Call: {call_price:.4f}")
print(f"Put:  {put_price:.4f}")
print(f"Selected {option_type} price: {selected_price:.4f}")

print("\n=== Greeks ===")
print(f"Call Delta: {c_delta:.4f}")
print(f"Put Delta:  {p_delta:.4f}")
print(f"Gamma:      {opt_gamma:.6f}")
print(f"Vega:       {opt_vega:.4f}")
print(f"Call Theta: {c_theta:.4f}")
print(f"Put Theta:  {p_theta:.4f}")
print(f"Selected {option_type} Delta: {selected_delta:.4f}")
print(f"Selected {option_type} Theta: {selected_theta:.4f}")

print("\n=== Diagnostics ===")
print(f"Forward price estimate: {forward:.4f}")
print(f"Call - Put:            {parity_lhs:.4f}")
print(f"S - K*e^(-rT):         {parity_rhs:.4f}")
print(f"Parity difference:     {abs(parity_lhs - parity_rhs):.8f}")

print("\n=== Spot Sensitivity ===")
spot_range = [0.8 * S, 0.9 * S, S, 1.1 * S, 1.2 * S]

for spot in spot_range:
    if option_type == "call":
        price = black_scholes_call(spot, K, T, r, sigma)
    else:
        price = black_scholes_put(spot, K, T, r, sigma)
    print(f"Spot {spot:.2f} -> {option_type.capitalize()} Price {price:.4f}")

print("\n=== Volatility Sensitivity ===")
for vol in [0.10, 0.15, 0.20, 0.25, 0.30]:
    call_vol_price = black_scholes_call(S, K, T, r, vol)
    put_vol_price = black_scholes_put(S, K, T, r, vol)
    print(f"Vol {vol:.2f} -> Call {call_vol_price:.4f} | Put {put_vol_price:.4f}")

# Profit at expiry plot
spot_grid = [x for x in range(int(0.5 * K), int(1.5 * K) + 1)]

if option_type == "call":
    profits = [call_profit_at_expiry(ST, K, premium) for ST in spot_grid]
    plot_title = "Call Profit at Expiry"
else:
    profits = [put_profit_at_expiry(ST, K, premium) for ST in spot_grid]
    plot_title = "Put Profit at Expiry"


from implied_vol import implied_vol_call

market_price = call_price

iv = implied_vol_call(S, K, T, r, market_price)

print("\n=== Implied Volatility ===")
print(f"Implied Vol: {iv:.4f}")

print("\n=== Delta Hedging ===")

hedge_shares = -c_delta
print(f"To delta hedge 1 call you short {abs(hedge_shares):.4f} shares")

print("\n=== Spot Scenario Analysis ===")

for shock in [-0.2, -0.1, 0, 0.1, 0.2]:
    spot = S * (1 + shock)
    price = black_scholes_call(spot, K, T, r, sigma)
    print(f"S = {spot:.2f} → Call = {price:.4f}")

    print("\n=== Time Decay ===")

for t in [1.0, 0.75, 0.5, 0.25, 0.1]:
    price = black_scholes_call(S, K, t, r, sigma)
    print(f"T = {t:.2f} → Call Price = {price:.4f}") 

plt.figure(figsize=(8, 5))
plt.plot(spot_grid, profits, label=f"{option_type.capitalize()} profit")
plt.axhline(0, linewidth=1)
plt.axvline(K, linestyle="--", linewidth=1, label="Strike")
plt.xlabel("Underlying price at expiry")
plt.ylabel("Profit")
plt.title(plot_title)
plt.legend()
plt.tight_layout()
plt.savefig("option_payoff.png", dpi=300)
plt.show()