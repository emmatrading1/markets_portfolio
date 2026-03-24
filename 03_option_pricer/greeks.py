import math
from scipy.stats import norm
from black_scholes import d1, d2


def call_delta(S, K, T, r, sigma):
    return norm.cdf(d1(S, K, T, r, sigma))


def put_delta(S, K, T, r, sigma):
    return norm.cdf(d1(S, K, T, r, sigma)) - 1


def gamma(S, K, T, r, sigma):
    d_1 = d1(S, K, T, r, sigma)
    return norm.pdf(d_1) / (S * sigma * math.sqrt(T))


def vega(S, K, T, r, sigma):
    d_1 = d1(S, K, T, r, sigma)
    return S * norm.pdf(d_1) * math.sqrt(T)


def call_theta(S, K, T, r, sigma):
    d_1 = d1(S, K, T, r, sigma)
    d_2 = d2(S, K, T, r, sigma)
    term_1 = -(S * norm.pdf(d_1) * sigma) / (2 * math.sqrt(T))
    term_2 = -r * K * math.exp(-r * T) * norm.cdf(d_2)
    return term_1 + term_2


def put_theta(S, K, T, r, sigma):
    d_1 = d1(S, K, T, r, sigma)
    d_2 = d2(S, K, T, r, sigma)
    term_1 = -(S * norm.pdf(d_1) * sigma) / (2 * math.sqrt(T))
    term_2 = r * K * math.exp(-r * T) * norm.cdf(-d_2)
    return term_1 + term_2