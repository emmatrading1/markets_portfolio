# IRS / Interest Rate Swaps — Notes

## What is a swap

Interest Rate Swap = contract where two parties exchange interest payments on a notional.

Most common structure:
fixed vs floating

One side:
receive fixed / pay floating

Other side:
pay fixed / receive floating

Floating leg references short-term rates:
SOFR (USD)
SONIA (GBP)
€STR (EUR)

Important: notional is NOT exchanged, only interest payments.

---

## Swap rate

The fixed rate is set so that:

PV fixed leg = PV floating leg

So at inception:

NPV ≈ 0

No money changes hands when the swap starts.

The fixed rate that achieves this is the **swap rate**.

---

## Intuition

Receiving fixed behaves like owning a bond.

Why:

you receive fixed cashflows.

So:

receiver fixed → long duration  
payer fixed → short duration

---

## PnL intuition

Receiver fixed:

rates ↓ → fixed payments become more valuable → MTM +

rates ↑ → fixed payments less attractive → MTM -

---

Payer fixed:

rates ↑ → fixed rate you're paying becomes cheap vs market → MTM +

rates ↓ → MTM -

---

## DV01

DV01 = dollar change in value for a 1bp move in rates.

Used to measure rate risk.

Example:

DV01 = 50k/bp

rates move -20bp

PnL ≈ 50k × 20 = +1m

Traders usually talk in DV01 rather than price.

---

## DV01-neutral trades

Traders often hedge to remove parallel rate exposure.

Example:

receive fixed 10Y
pay fixed 5Y

size positions so DV01 exposure cancels.

Then the trade is about curve shape rather than rate direction.

Example: 5s10s steepener.

---

## Swap spreads

swap spread = swap rate − government bond yield (same maturity)

example:

10Y swap = 4.10%
10Y treasury = 4.00%

spread = 10bp

Drivers:

- treasury demand / flight to safety
- dealer balance sheet constraints
- hedging flows from investors

---

## Closing a swap

To exit a swap position:

enter the opposite swap with same maturity and notional.

Example:

original trade:
receive fixed 5Y

close:
pay fixed 5Y

cashflows offset → position flat → MTM realized.

---

## why swaps matter

core instrument in rates markets.

Used to:
- hedge interest rate exposure
- trade curve shape
- manage duration
- express macro views on rates