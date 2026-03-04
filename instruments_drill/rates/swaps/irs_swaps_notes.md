# swaps / IRS notes

interest rate swap = exchange of interest payments on a notional  
no notional exchange, just the interest flows

classic structure:
fixed vs floating

one side receive fixed / pay float  
other side pay fixed / receive float

floating leg usually something like SOFR / SONIA / €STR depending on currency


swap rate

fixed rate set so that PV fixed leg = PV floating leg

so when the trade starts:

NPV ≈ 0


intuition

receiving fixed basically behaves like being long a bond

because you're receiving fixed cashflows

so:

receiver fixed = long duration  
payer fixed = short duration


P&L intuition

receiver fixed

rates ↓ → good  
fixed rate you locked becomes more valuable

rates ↑ → bad


payer fixed

rates ↑ → good  
because fixed rate you're paying becomes cheap vs market

rates ↓ → bad


DV01

DV01 = $ change for 1bp move in rates

example

DV01 = 50k/bp

rates move -20bp

PnL ≈ +1m


traders usually think in DV01 not price


DV01 neutral

common thing on desks

example

receive 10Y
pay 5Y

size positions so DV01 cancels

then you're not trading direction anymore  
you're trading the curve

ex: 5s10s steepener


swap spread

swap rate - gov bond yield (same maturity)

example

10Y swap = 4.10  
10Y treasury = 4.00

spread = 10bp

moves with:

treasury demand
dealer balance sheet
hedging flows


closing a swap

enter opposite swap

ex

receive fixed 5Y  
close = pay fixed 5Y

cashflows offset → position flat → MTM locked


why swaps matter

core rates instrument

used for

hedging duration
trading curve shape
macro views on rates
balance sheet management