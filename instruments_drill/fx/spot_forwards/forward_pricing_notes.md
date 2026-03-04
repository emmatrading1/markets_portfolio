forward pricing — hull ch5 notes

main idea:
forward price is not a prediction of the future price.
it is set by arbitrage.

at initiation → forward value = 0

why?
because delivery price is chosen so that no arbitrage exists.

if forward price was wrong you could construct a risk-free profit using spot + borrowing.

example intuition:

strategy 1
buy asset today
borrow money to finance it

cost at maturity
S0 * e^(rT)

strategy 2
enter forward contract
pay F0 at maturity

→ must be same outcome

so

F0 = S0 * e^(rT)

if forward price too high

F0 > S0 e^(rT)

arbitrage:

t0
borrow S0
buy asset
short forward

tT
deliver asset
receive F0
repay loan

profit = F0 − S0 e^(rT)

---

dividends

formula becomes

F0 = S0 e^((r − q)T)

q = dividend yield

intuition

holding stock → you receive dividends
forward buyer → does NOT receive them

so owning spot is more valuable

→ forward price lower

large dividends → forward cheaper vs spot

---

FX forwards

F0 = S0 e^((rd − rf)T)

rd = domestic rate
rf = foreign rate

logic:

holding foreign currency earns foreign interest rate

so if foreign rates high
forward price lower.

---

cost of carry idea

forward price basically

spot + cost of holding asset

carry includes

interest rate
storage costs
dividends
foreign interest rate

effects

rates ↑ → forward ↑

dividends ↑ → forward ↓

storage costs ↑ → forward ↑

---

important thing

forward price ≠ expected future price

forward price
→ determined by arbitrage

expected future price
→ determined by expectations / probabilities

---

quick example

S0 = 2000
r = 4%

F0 ≈ 2081.62

if dividend yield = 1%

F0 ≈ 2060.91

dividends reduce forward price

---

things interviewers often ask

why forward value = 0 at initiation

difference forward price vs expected price

what arbitrage if forward too high

why dividends reduce forward prices

why storage costs increase forward prices