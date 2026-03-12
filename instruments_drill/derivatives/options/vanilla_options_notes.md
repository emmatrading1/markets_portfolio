### **options core notes**
### **core idea**
option = right but not obligation to trade an asset at a predetermined price (strike)
call → right to buy asset at strike K
put → right to sell asset at strike K
buyer pays premium upfront
maximum loss for option buyer = premium
### **value at expiration**
call payoff = max(ST − K, 0)
put payoff = max(K − ST, 0)
profit = payoff − premium
### **basic intuition**
call → benefits from price increase
put → benefits from price decrease
call upside = unlimited
put upside = large when price falls
### **call example**
S0 = 100
K = 100
premium = 6
ST = 95 → payoff = 0 → profit = −6
ST = 108 → payoff = 8 → profit = 2
ST = 150 → payoff = 50 → profit = 44
### **break-even**
call break-even = K + premium
→ 106
### **put example**
S0 = 100
K = 100
premium = 5
ST = 120 → payoff = 0 → profit = −5
ST = 95 → payoff = 5 → profit = 0
ST = 60 → payoff = 40 → profit = 35
### **break-even**
put break-even = K − premium
→ 95
### **straddle strategy**
long call + long put (same strike and maturity)
strategy profits from large price movements in either direction
profit if |ST − K| > total premiums
loss if price stays near strike
→ strategy trades volatility rather than direction
### **put-call parity**
relationship between call, put, stock and bond
C − P = S − Ke^(−rT)
C = call price
P = put price
S = stock price
K = strike
r = risk-free rate
T = maturity
### **synthetic positions**
options can replicate stock exposure
long call + short put = synthetic long stock
short call + long put = synthetic short stock
### **intuition**
if stock rises
call gains value
put expires worthless
→ payoff behaves like owning stock
if stock falls
call expires worthless
short put loses value
→ payoff behaves like stock loss
### **trader takeaway**
options allow traders to
replicate stock exposure
trade volatility
construct synthetic positions
hedge portfolios

### **arbitrage intuition**

put-call parity must hold in efficient markets

C − P = S − Ke^(−rT)

if equality does not hold → arbitrage opportunity

example logic

if

C − P > S − Ke^(−rT)

left side too expensive

strategy

sell call
buy put
buy stock
borrow PV(K)

reverse if

C − P < S − Ke^(−rT)

left side too cheap

buy call
sell put
sell stock
lend PV(K)

goal

lock risk-free profit until maturity


### **lower bounds**

options cannot be priced below certain theoretical limits

call lower bound

C ≥ max(0, S − Ke^(−rT))

put lower bound

P ≥ max(0, Ke^(−rT) − S)

intuition

call must be worth at least intrinsic value of buying the asset later instead of now

put must be worth at least intrinsic value of selling the asset later instead of now

if price violates bound → arbitrage possible


### **options greeks introduction**

greeks measure sensitivity of option price to different risk factors

main greeks

delta
gamma
theta
vega
rho


### **delta**

delta measures sensitivity of option price to underlying price

Δ = ∂C / ∂S

call delta

0 → 1

put delta

0 → −1

intuition

delta roughly measures how much option price moves if the underlying moves by 1

deep ITM call

Δ ≈ 1

deep OTM call

Δ ≈ 0


### **gamma**

gamma measures how fast delta changes when the underlying price moves

Γ = ∂²C / ∂S²

gamma highest

near the strike
near maturity

importance

large gamma → delta changes very quickly


### **theta**

theta measures time decay

Θ = ∂C / ∂t

options lose value as maturity approaches

theta usually negative for option buyers


### **vega**

vega measures sensitivity to volatility

ν = ∂C / ∂σ

higher volatility

→ higher option value

because probability of large price moves increases


### **rho**

rho measures sensitivity to interest rates

ρ = ∂C / ∂r

calls

rates ↑ → option value ↑

puts

rates ↑ → option value ↓


### **trader takeaway**

options allow traders to

replicate stock exposure
trade volatility
construct synthetic positions
hedge portfolios
express macro views with convex payoff


### **instrument drill progress**

today

reviewed core option mechanics
reviewed payoff logic
worked through put-call parity arbitrage logic
introduced greeks conceptually


### **next drill plan**

delta hedging mechanics
gamma exposure examples
volatility intuition
implied vs realized volatility
option pricing intuition