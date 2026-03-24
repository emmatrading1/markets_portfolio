import math
from black_scholes import black_scholes_call
from greeks import vega


def implied_vol_call(S, K, T, r, market_price, initial_vol=0.2, tol=1e-6, max_iter=100):

    sigma = initial_vol

    for _ in range(max_iter):

        price = black_scholes_call(S, K, T, r, sigma)
        v = vega(S, K, T, r, sigma)

        diff = price - market_price

        if abs(diff) < tol:
            return sigma

        sigma = sigma - diff / v

    return sigma