# 4.10 — Kawasaki algorithm: local version

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| 🔶 at least one of 4.9 / 4.10 / 4.11 | simulation | [p. 42–43](../../Coursenotes/monte_carlo_2025.pdf#page=42) | ⬜ todo |

## Question

Conserved-order-parameter Ising model: the Kawasaki algorithm conserves the total
magnetization $M = \sum_i s_i$. Pick two **neighbouring** spins at random; if equal, do
nothing; if different, try to swap them with the Metropolis rule.

Lattice $L_x = 200$, $L_y = 50$; **fixed** boundary conditions in $y$ (top and bottom rows
fixed and never selected), **periodic** in $x$. $T_c = 2/\ln(1+\sqrt2)\approx 2.269$.

Initial configuration Fig. 14(a): upper half $+$, lower half $-$, straight horizontal interface.

**Sub-questions**

- [ ] (a) Start from Fig. 14(a) at $T = 0.9\,T_c$; run $N$ MC steps and determine $N_{acc}$, the number of swaps actually performed.
- [ ] (b) Determine $N_{acc}/N$ at $T = 0.5\,T_c$, $1.2\,T_c$, $2.5\,T_c$. Does it increase or decrease with $T$? Does this match expectations?
- [ ] (c) From Fig. 14(a), plot the energy per spin vs. number of sweeps at $T = 0.9\,T_c$ and estimate the equilibration time.

## Relevant topics

- Conserved order parameter Ising model, Kawasaki dynamics — [§2.10, p. 21](../../Coursenotes/monte_carlo_2025.pdf#page=21)
- Metropolis acceptance — [§2.4, p. 10](../../Coursenotes/monte_carlo_2025.pdf#page=10)
- Equilibration — [§2.5, p. 11](../../Coursenotes/monte_carlo_2025.pdf#page=11)
- Interfaces, phase separation (canonical vs. grand-canonical ensemble)

## Course material

- Problem statement: [notes p. 42](../../Coursenotes/monte_carlo_2025.pdf#page=42), Fig. 14 on [p. 43](../../Coursenotes/monte_carlo_2025.pdf#page=43)
- Follow-up: [4.11 non-local version](../4.11-kawasaki-nonlocal/)

## Deliverables for the report

- Table of $N_{acc}/N$ vs. $T/T_c$ (clarify whether $N$ counts all attempts or only unequal pairs).
- $e(t)$ vs. sweeps at $0.9\,T_c$ with $\tau_{eq}$; snapshots of the interface.

## Implementation notes

- With fixed rows in $y$, the energy difference of a swap must include bonds to the fixed rows.
- $\Delta E$ for a swap of opposite neighbours: compute from the neighbours of both sites, excluding their mutual bond.

## Possible exam questions

- Why is magnetization conserved, and which physical systems does this model (lattice gas, binary alloy)?
- Why is local Kawasaki dynamics slow?

## Results & notes

_To be filled in._

## AI usage log

_To be filled in._
