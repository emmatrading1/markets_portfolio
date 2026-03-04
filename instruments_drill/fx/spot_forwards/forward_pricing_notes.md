# Forward pricing — notes (Hull Ch.5)

today focus: how forward prices are determined

key idea: forward price is NOT a prediction of the future price.  
it is determined by arbitrage.

when you enter a forward contract, its value = 0.

why?  
because the delivery price is set so that no arbitrage opportunity exists.

---

## basic forward pricing (no income asset)

formula

F0 = S0 * e^(rT)

S0 = spot price today  
r = risk-free rate  
T = maturity

intuition:

two strategies must give the same result:

strategy 1  
buy asset today → finance it by borrowing

cost at maturity = S0 * e^(rT)

strategy 2  
enter forward contract today → pay F0 at maturity

no arbitrage → these must be equal

therefore

F0 = S0 * e^(rT)

---

## if forward price is wrong

if forward price too high:

F0 > S0 e^(rT)

arbitrage:

t0
borrow S0  
buy asset  
short forward

tT
deliver asset into forward  
receive F0  
repay loan S0 e^(rT)

profit = F0 − S0 e^(rT)

risk-free.

---

## assets with income (dividends)

formula

F0 = S0 e^((r − q)T)

q = dividend yield

intuition:

owning the stock today gives you dividends  
forward buyer does NOT receive dividends

so owning spot is more valuable

→ forward price must be lower.

large dividends → forward price decreases.

---

## FX forwards

formula

F0 = S0 e^((rd − rf)T)

rd = domestic interest rate  
rf = foreign interest rate

intuition:

holding foreign currency earns the foreign interest rate.

higher foreign rate → forward price lower.

---

## cost of carry idea

forward price = spot + cost of carrying the asset.

carry includes:

interest rate  
storage costs  
dividends  
foreign interest rate (FX)

examples:

interest rate ↑ → forward price ↑

dividends ↑ → forward price ↓

storage cost ↑ → forward price ↑

---

## important distinction

forward price ≠ expected future price

expected future price  
→ depends on market expectations

forward price  
→ determined by arbitrage.

---

## small example

S0 = 2000  
r = 4%  
T = 1

F0 = 2000 e^(0.04) ≈ 2081.62

with dividend yield q = 1%

F0 = 2000 e^(0.03) ≈ 2060.91

dividends reduce forward price.

---

## interview questions to know

why is forward value zero at initiation?

what determines the forward price?

what arbitrage if forward price too high?

difference between forward price and expected future price?

why do dividends reduce forward prices?

why do storage costs increase forward prices?