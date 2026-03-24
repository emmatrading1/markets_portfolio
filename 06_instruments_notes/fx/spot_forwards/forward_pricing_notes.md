## FX SPOT & FORWARD PRICING

### core idea
forward price ≠ prediction of future spot price → it is determined by arbitrage  
forward contracts lock an exchange rate today for a transaction at a future date

### value at initiation
forward value = 0 at initiation → forward price chosen so that no arbitrage exists

### pricing intuition
two equivalent strategies

1 → buy asset today and finance it  
2 → enter forward contract today  

both strategies deliver the asset at maturity → forward price must reflect cost of carrying the asset

### forward pricing formula
F₀ = S₀ * e^(rT)

S₀ = spot price  
r = risk-free rate  
T = maturity

intuition → buying today requires financing → forward embeds that cost

### income / dividend adjustment
if the asset generates income

F₀ = S₀ * e^((r − q)T)

q = dividend yield

intuition → owning the asset generates income → forward buyer does not receive it → forward price decreases

### FX forward pricing
F₀ = S₀ * e^((rd − rf)T)

rd = domestic interest rate  
rf = foreign interest rate

intuition → forward adjusts spot for the interest rate differential between currencies

### forward premium / discount
higher interest rate currency → forward discount  
lower interest rate currency → forward premium

example

if USD rate > EUR rate

USD trades at forward discount  
EUR trades at forward premium  
→ EUR/USD forward > spot

### covered interest rate parity (CIP)
spot, forward and interest rates must satisfy

F = S * e^((rd − rf)T)

otherwise arbitrage exists between FX and money markets

CIP ensures no risk-free profit from borrowing in one currency and investing in another

### forward arbitrage logic
if forward > fair value → asset overpriced in forward market

trade

borrow foreign currency  
convert to domestic at spot  
invest domestic  
sell forward

if forward < fair value → asset underpriced in forward market

trade

borrow domestic currency  
convert to foreign  
invest foreign  
buy forward

### trader rule
forward too high → sell forward  
forward too low → buy forward

### why this matters
FX forwards link

spot FX  
interest rates  
funding markets

used for

hedging FX exposure  
pricing cross-currency flows  
funding and arbitrage trades

### forward value (after initiation)
at initiation → value = 0

after → value changes with forward price

V = (F_market − F_contract) discounted

long forward:
F ↑ → gain  
F ↓ → loss

short forward:
F ↓ → gain  
F ↑ → loss


### FX quotation (base / quote)
currency pairs are quoted as:

BASE / QUOTE

BASE = first currency  
QUOTE = second currency

example:
EUR/USD = 1.10 → 1 EUR = 1.10 USD


### trading interpretation
BUY → receive BASE, pay QUOTE  
SELL → deliver BASE, receive QUOTE


### arbitrage construction (clean version)
forward too high:
SELL → deliver BASE → borrow BASE → convert → invest → sell forward
forward too low:
BUY → deliver QUOTE → borrow QUOTE → convert → invest → buy forward