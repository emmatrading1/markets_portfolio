import numpy as np
import math
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):
    
    d1 = (np.log(S/K) + (r + 0.5 * sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    call = S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)

    return call


def black_scholes_put(S, K, T, r, sigma):

    d1 = (np.log(S/K) + (r + 0.5 * sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    put = K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return put

    import math
from scipy.stats import norm


def d1(S, K, T, r, sigma):
    return (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))


def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma * math.sqrt(T)


def black_scholes_call(S, K, T, r, sigma):
    d_1 = d1(S, K, T, r, sigma)
    d_2 = d2(S, K, T, r, sigma)
    return S * norm.cdf(d_1) - K * math.exp(-r * T) * norm.cdf(d_2)


def black_scholes_put(S, K, T, r, sigma):
    d_1 = d1(S, K, T, r, sigma)
    d_2 = d2(S, K, T, r, sigma)
    return K * math.exp(-r * T) * norm.cdf(-d_2) - S * norm.cdf(-d_1)