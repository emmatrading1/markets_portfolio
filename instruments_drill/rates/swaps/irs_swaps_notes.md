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