## core idea

option = right but not obligation to trade an asset at a predetermined price (strike)

call → right to buy asset at strike K  
put → right to sell asset at strike K  

buyer pays premium upfront  
maximum loss for option buyer = premium


## value at expiration

call payoff = max(ST − K, 0)  
put payoff = max(K − ST, 0)

profit = payoff − premium


## basic intuition

call → benefits from price increase  
put → benefits from price decrease  

call upside = unlimited  
put upside = large when price falls


## call example

S0 = 100  
K = 100  
premium = 6

ST = 95 → payoff = 0 → profit = −6  
ST = 108 → payoff = 8 → profit = 2  
ST = 150 → payoff = 50 → profit = 44

break-even

call break-even = K + premium  
→ 106


## put example

S0 = 100  
K = 100  
premium = 5

ST = 120 → payoff = 0 → profit = −5  
ST = 95 → payoff = 5 → profit = 0  
ST = 60 → payoff = 40 → profit = 35

break-even

put break-even = K − premium  
→ 95


## straddle strategy

long call + long put (same strike and maturity)

strategy profits from large price movements in either direction

profit if

|ST − K| > total premiums

loss if price stays near strike

→ strategy trades volatility rather than direction


## put-call parity

relationship between call, put, stock and bond

C − P = S − Ke^(−rT)

C = call price  
P = put price  
S = stock price  
K = strike  
r = risk-free rate  
T = maturity


## synthetic positions

options can replicate stock exposure

long call + short put = synthetic long stock  
short call + long put = synthetic short stock


## intuition

if stock rises

call gains value  
put expires worthless

→ payoff behaves like owning stock

if stock falls

call expires worthless  
short put loses value

→ payoff behaves like stock loss


## trader takeaway

options allow traders to

replicate stock exposure  
trade volatility  
construct synthetic positions  
hedge portfolios