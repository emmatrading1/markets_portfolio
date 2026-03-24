### swap definition

interest rate swap = exchange of interest payments on a notional → no principal exchange, only interest flows

structure → fixed leg vs floating leg → one side receive fixed / pay float, other side pay fixed / receive float

floating leg usually indexed to SOFR / SONIA / €STR depending on currency


### swap rate

fixed rate chosen so that PV(fixed leg) = PV(floating leg) → therefore when trade starts → NPV ≈ 0


### intuition

receiving fixed behaves like long a bond → receiving fixed cashflows

receiver fixed → long duration  
payer fixed → short duration


### P&L intuition

receiver fixed → rates ↓ good (locked fixed rate becomes valuable) → rates ↑ bad

payer fixed → rates ↑ good (paying fixed cheaper than market) → rates ↓ bad


### DV01

DV01 = $ change in value for 1bp move in rates

example → DV01 = 50k/bp → rates move -20bp → PnL ≈ +1m

traders think in DV01 rather than price


### DV01 neutral trades

common desk structure → hedge directional risk

example → receive 10Y swap + pay 5Y swap → size positions so DV01 cancels

result → not trading rates level anymore → trading curve shape (ex: 5s10s steepener)


### swap spread

swap spread = swap rate − government bond yield (same maturity)

example → 10Y swap 4.10 vs 10Y treasury 4.00 → spread = 10bp

drivers → treasury demand / dealer balance sheet constraints / hedging flows


### closing a swap

close position by entering opposite swap

example → receive fixed 5Y → close by paying fixed 5Y → cashflows offset → MTM locked


### why swaps matter

core instrument of rates markets → used for duration hedging, curve trading, macro positioning, bank balance sheet management



### swap valuation intuition

swap can be decomposed into → fixed bond − floating bond

receive fixed swap → long fixed bond / short floating bond

pay fixed swap → short fixed bond / long floating bond

because floating coupons reset to market rates → floating bond value stays close to par

therefore after each reset date → floating leg ≈ notional


### duration intuition

receive fixed → behaves like holding a fixed rate bond → positive duration

pay fixed → behaves like shorting a bond → negative duration

rates ↓ → receive fixed gains value

rates ↑ → pay fixed gains value


### curve trades

swap traders often combine maturities to trade curve shape

example → receive 10Y swap + pay 5Y swap

if DV01 sized correctly → overall rate exposure ≈ neutral

position then profits from changes in slope of curve

receive long maturity / pay short maturity → steepener

receive short maturity / pay long maturity → flattener


### curve notation

yield curve spreads written as → short maturity first

2s10s = 10Y yield − 2Y yield

5s10s = 10Y yield − 5Y yield

10s30s = 30Y yield − 10Y yield


### steepening vs flattening

steepening → long maturity yield rises relative to short maturity yield

example → 5s10s increases

flattening → long maturity yield falls relative to short maturity yield

example → 5s10s decreases


### DV01 sizing logic

different maturities have different rate sensitivity

example

DV01 30Y ≈ larger than DV01 10Y

therefore traders size notionals so that

DV01 long ≈ DV01 short

result → trade isolates curve movement instead of overall rate direction

### P&L estimation (DV01 use)

P&L ≈ DV01 × Δrates

example:
DV01 = 15k/bp  
rates move +10bp → P&L ≈ −150k (if long duration)

DV01 gives a first-order approximation of P&L


### convexity (important limitation)

DV01 is linear approximation

for large rate moves → convexity matters

receive fixed (long bond) → positive convexity  
pay fixed (short bond) → negative convexity

→ DV01 becomes less accurate for large moves