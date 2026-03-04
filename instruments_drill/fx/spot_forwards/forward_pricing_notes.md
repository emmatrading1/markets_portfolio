**core idea**

forward price is not a prediction of the future price

it is determined by arbitrage


**value at initiation**

forward value = 0 when contract starts

why

delivery price chosen so that no arbitrage exists


**basic intuition**

two strategies must give same outcome

1 → buy asset today + borrow money  
2 → enter forward contract today

so

forward price must equal cost of buying and carrying the asset


**basic formula**

F0 = S0 * e^(rT)

S0 = spot price  
r = risk-free rate  
T = maturity


**arbitrage if forward too high**

if

F0 > S0 e^(rT)

trade

t0  
borrow S0 → buy asset → short forward

tT  
deliver asset → receive F0 → repay loan

profit = F0 − S0 e^(rT)


**dividends**

if asset pays dividends

formula becomes

F0 = S0 e^((r − q)T)

q = dividend yield

intuition

owning stock → you receive dividends  
forward buyer → does not

so spot more valuable → forward cheaper

large dividends → lower forward price


**FX forwards**

formula

F0 = S0 e^((rd − rf)T)

rd = domestic rate  
rf = foreign rate

logic

holding foreign currency earns foreign interest rate

if foreign rates higher → forward price lower


**cost of carry**

forward price = spot + cost of carrying asset

carry includes

interest rates  
storage costs  
dividends  
foreign interest rate


effects

rates ↑ → forward ↑  
dividends ↑ → forward ↓  
storage costs ↑ → forward ↑


**important distinction**

forward price ≠ expected future price

forward price → determined by arbitrage  
expected price → determined by market expectations


**quick example**

S0 = 2000  
r = 4%

F0 ≈ 2081.62

with dividend yield 1%

F0 ≈ 2060.91

dividends reduce forward price


**interview questions**

why forward value = 0 at initiation  
difference between forward price and expected price  
arbitrage if forward price too high  
why dividends reduce forward price  
why storage costs increase forward price