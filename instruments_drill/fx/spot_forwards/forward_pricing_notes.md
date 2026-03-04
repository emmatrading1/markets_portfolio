### core idea

forward price ≠ prediction of future price → it is determined by arbitrage


### value at initiation

forward value = 0 when contract starts → delivery price chosen so that no arbitrage exists


### basic intuition

two equivalent strategies

1 → buy asset today + borrow money  
2 → enter forward contract today

→ same future outcome → therefore forward price must equal cost of buying and carrying the asset


### forward pricing formula

F0 = S0 * e^(rT)

S0 = spot price → r = risk-free rate → T = maturity


### arbitrage if forward too high

if F0 > S0 e^(rT)

trade → borrow S0 → buy asset → short forward

at maturity → deliver asset into forward → receive F0 → repay loan

profit = F0 − S0 e^(rT)


### dividends

if asset pays dividends

F0 = S0 e^((r − q)T)

q = dividend yield

intuition → owning stock gives dividends → forward buyer does not → spot becomes more valuable → forward price lower


### FX forwards

F0 = S0 e^((rd − rf)T)

rd = domestic interest rate → rf = foreign interest rate

higher foreign rate → forward price lower


### cost of carry intuition

forward price ≈ spot + cost of carrying asset

carry includes → interest rate / storage costs / dividends / foreign interest rate

effects → rates ↑ forward ↑ | dividends ↑ forward ↓ | storage costs ↑ forward ↑


### important distinction

forward price → determined by arbitrage  
expected future price → determined by market expectations


### quick example

S0 = 2000 → r = 4%

F0 ≈ 2081.62

if dividend yield = 1%

F0 ≈ 2060.91 → dividends reduce forward price


### interview questions

why forward value = 0 at initiation  
difference forward price vs expected price  
arbitrage if forward price too high  
why dividends reduce forward prices  
why storage costs increase forward prices