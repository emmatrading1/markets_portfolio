### **futures definition**

a futures contract is an agreement to buy or sell an asset at a predetermined price at a future date.

futures are standardized contracts traded on exchanges and a clearinghouse guarantees the trade between participants.

profits and losses are settled daily through **mark-to-market**.



### **long vs short futures**

long futures  
→ obligation to buy the underlying asset at maturity  
→ profit if the price rises

short futures  
→ obligation to sell the underlying asset at maturity  
→ profit if the price falls



### **daily mark-to-market**

futures positions are settled every day.

p&l = (today futures price − yesterday futures price) × contract size

profits are credited to the margin account  
losses are deducted from the margin account



### **margin system**

initial margin  
→ collateral deposited when opening a futures position

maintenance margin  
→ minimum balance required in the margin account

if the account balance falls below maintenance margin → margin call

the trader must deposit funds to restore the account to the initial margin level



### **futures pricing intuition**

futures prices reflect the **cost of carry**

F ≈ S + financing cost + storage cost − convenience yield

because of these costs futures prices can differ from spot prices



### **hedging with futures**

futures allow market participants to lock a future price

short hedge  
→ used when the agent will **sell an asset later**

long hedge  
→ used when the agent will **buy an asset later**



### **short hedge intuition**

example: a farmer will sell wheat in six months

risk  
→ wheat price may fall

solution  
→ short futures today

if price falls the loss in the spot market is offset by a gain in futures



### **long hedge intuition**

example: a company will buy oil in the future

risk  
→ oil price may rise

solution  
→ long futures today

if price rises the higher purchase cost is offset by a gain in futures



### **basis**

basis = spot price − futures price

basis measures the difference between the physical market and the futures market



### **basis behavior**

as the futures contract approaches maturity the futures price converges toward the spot price

therefore the basis tends toward **zero at expiration**



### **basis risk**

hedging removes most price risk but not basis risk

basis risk = uncertainty about the basis when the hedge is closed

final hedge effectiveness depends on the basis at that moment



### **basis strengthening vs weakening**

basis strengthening  
→ basis moves **closer to zero**

basis weakening  
→ basis moves **further from zero**



### **impact on hedge performance**

short hedge

basis strengthens → hedge performs better  
basis weakens → hedge performs worse


long hedge

basis weakens → hedge performs better  
basis strengthens → hedge performs worse



### **optimal hedge ratio**

when the futures asset differs from the hedged asset the hedge ratio may differ from 1

the optimal hedge ratio minimizes the variance of the hedged position

h* = ρ × (σS / σF)

ρ = correlation between spot and futures price changes  
σS = volatility of spot prices  
σF = volatility of futures prices



### **interpretation**

if spot is more volatile than futures  
→ hedge ratio > 1

if futures are more volatile than spot  
→ hedge ratio < 1



### **number of futures contracts**

N* = h* × (QA / QF)

QA = size of asset exposure  
QF = size of one futures contract



### **cross hedging**

cross hedge = hedging an asset using futures on a different but related asset

example

exposure → jet fuel  
futures used → crude oil futures

because assets are not identical correlation is imperfect and basis risk increases



### **stack and roll hedging**

when the exposure horizon is longer than available futures maturities traders use a **stack-and-roll strategy**

process

open futures hedge  
close the position before expiration  
open a new futures contract  
repeat until exposure ends



### **roll risk**

rolling futures introduces **roll risk**

when the hedge is rolled the new futures contract may be priced very differently from the previous one

changes in the futures curve (contango or backwardation) can affect the cost of maintaining the hedge



### **key intuition**

a futures hedge locks the futures price but **does not lock the basis**

final hedge effectiveness depends on

basis movements  
correlation between assets  
roll conditions when futures are renewed