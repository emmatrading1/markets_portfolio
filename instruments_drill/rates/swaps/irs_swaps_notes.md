**swap definition**

interest rate swap = exchange of interest payments on a notional  
no notional exchange → only interest flows

classic structure → fixed vs floating

one side: receive fixed / pay float  
other side: pay fixed / receive float

floating leg usually indexed to SOFR / SONIA / €STR depending on currency


**swap rate**

fixed rate chosen so that

PV fixed leg = PV floating leg

so when trade starts

NPV ≈ 0


**intuition**

receiving fixed behaves like being long a bond

reason → you're receiving fixed cashflows

so

receiver fixed → long duration  
payer fixed → short duration


**P&L intuition**

receiver fixed

rates ↓ → good  
locked fixed rate becomes more valuable

rates ↑ → bad

payer fixed

rates ↑ → good  
fixed rate you're paying becomes cheap vs market

rates ↓ → bad


**DV01**

DV01 = dollar value of a 1bp move

how much PnL changes if rates move 1bp

example

DV01 = 50k/bp  
rates move -20bp

PnL ≈ +1m

traders usually think in DV01 rather than price


**DV01 neutral**

very common on desks

example

receive 10Y swap  
pay 5Y swap

sizes chosen so DV01 cancels

→ not trading direction anymore  
→ trading curve shape


example trade

5s10s steepener


**swap spread**

swap spread = swap rate − government bond yield

example

10Y swap = 4.10  
10Y treasury = 4.00

spread = 10bp

drivers

treasury demand  
dealer balance sheet  
hedging flows


**closing a swap**

close position by entering opposite swap

example

receive fixed 5Y  
close → pay fixed 5Y

cashflows offset  
position becomes flat  
MTM locked


**why swaps matter**

core instrument in rates markets

used for

hedging duration  
trading curve shape  
macro views on rates  
bank balance sheet management