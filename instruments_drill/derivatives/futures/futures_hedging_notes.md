## Futures Definition

A futures contract is an agreement to buy or sell an asset at a predetermined price at a future date.

Futures are standardized contracts traded on exchanges.  
A clearinghouse guarantees the trade between participants.

Profits and losses are settled daily through a mechanism called **mark-to-market**.



## Long vs Short Futures

Long futures  
→ obligation to buy the underlying asset at maturity  
→ profit if the price rises.

Short futures  
→ obligation to sell the underlying asset at maturity  
→ profit if the price falls.



## Daily Mark-to-Market

Futures positions are settled every day.

P&L is calculated as:

P&L = (today futures price − yesterday futures price) × contract size

Profits are credited to the margin account.  
Losses are deducted from the margin account.



## Margin System

Initial margin  
→ collateral deposited when opening a futures position.

Maintenance margin  
→ minimum balance required in the margin account.

If the account balance falls below the maintenance margin, a **margin call** occurs.

The trader must deposit additional funds to restore the account to the initial margin level.



## Futures Pricing Intuition

Futures prices reflect the **cost of carry**.

F ≈ S + financing cost + storage cost − convenience yield

Because of these costs, the futures price can differ from the spot price.



## Hedging with Futures

Futures allow market participants to lock a future price.

Two main hedge types exist.

Short hedge  
→ used when the agent will **sell an asset later**.

Long hedge  
→ used when the agent will **buy an asset later**.



## Short Hedge Intuition

Example: a farmer will sell wheat in 6 months.

Risk  
→ wheat prices may fall.

Solution  
→ short futures today.

If prices fall, the loss in the spot market is offset by a gain in futures.



## Long Hedge Intuition

Example: a company will buy oil in the future.

Risk  
→ oil prices may rise.

Solution  
→ long futures today.

If prices rise, the higher purchase cost is offset by a gain in futures.



## Basis

Basis measures the difference between spot and futures prices.

Basis = Spot price − Futures price



## Basis Behavior

As the futures contract approaches maturity, the futures price converges toward the spot price.

Therefore the basis tends to **zero at expiration**.



## Basis Risk

Futures hedging eliminates most price risk but not basis risk.

Basis risk = uncertainty about the basis when the hedge is closed.

The final effectiveness of the hedge depends on the basis at that moment.



## Basis Strengthening vs Weakening

Basis strengthening  
→ basis moves **closer to zero**

Basis weakening  
→ basis moves **further from zero**



## Impact on Hedge Performance

Short hedge

Basis strengthens → hedge performs better  
Basis weakens → hedge performs worse


Long hedge

Basis weakens → hedge performs better  
Basis strengthens → hedge performs worse



## Optimal Hedge Ratio

When the futures asset differs from the hedged asset, the hedge ratio may differ from 1.

The optimal hedge ratio minimizes the variance of the hedged position.

h* = ρ × (σS / σF)

ρ = correlation between spot and futures price changes  
σS = volatility of spot prices  
σF = volatility of futures prices



## Interpretation

If spot is more volatile than futures  
→ hedge ratio > 1

If futures are more volatile than spot  
→ hedge ratio < 1



## Number of Futures Contracts

The number of futures contracts used in the hedge is:

N* = h* × (QA / QF)

QA = size of the asset exposure  
QF = size of one futures contract



## Cross Hedging

A cross hedge occurs when the asset being hedged is different from the underlying asset of the futures contract.

Example

Exposure: jet fuel  
Futures used: crude oil futures

Because the assets are not identical, correlation is imperfect and basis risk increases.



## Stack and Roll Hedging

When the exposure horizon is longer than the maturity of available futures contracts, traders use a **stack and roll strategy**.

The process is:

1. open a futures hedge  
2. close the position before expiration  
3. open a new futures contract  
4. repeat until the exposure ends



## Roll Risk

Rolling futures introduces **roll risk**.

When the hedge is rolled, the new futures price may differ significantly from the previous contract.

Changes in the futures curve (contango or backwardation) can affect the cost of maintaining the hedge.



## Key Intuition

A futures hedge locks the futures price but **does not lock the basis**.

Final hedge effectiveness depends on:

- basis movements
- correlation between assets
- roll conditions when futures are renewed