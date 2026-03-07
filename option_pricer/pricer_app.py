from black_scholes import black_scholes_call, black_scholes_put

# Example parameters
S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2

call_price = black_scholes_call(S, K, T, r, sigma)
put_price = black_scholes_put(S, K, T, r, sigma)

print("Call price:", round(call_price, 4))
print("Put price:", round(put_price, 4))