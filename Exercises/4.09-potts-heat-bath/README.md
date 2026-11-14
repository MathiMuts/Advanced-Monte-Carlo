# 4.9 — Heat bath algorithm for the Potts model

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| 🔶 at least one of 4.9 / 4.10 / 4.11 | analytical + simulation | [p. 41–42](../../Coursenotes/monte_carlo_2025.pdf#page=41) | ⬜ todo |

## Question

$q$-state Potts model: $s_i \in \{0, 1, \dots, q-1\}$, $E = -J\sum_{\langle ij\rangle}\delta_{s_is_j}$
(nearest neighbours, $J>0$). $q = 2$ is equivalent to Ising. For $q>2$ there is a transition
from an ordered ("ferromagnetic") phase to a disordered high-$T$ phase.

**Heat bath:** single-spin update. For spin $s_k$, let $E_m$ be the energy when $s_k = m$.
The selection probability to go from $\mu$ to $\nu$ (where $s_k = n$ in $\nu$) is

$$g(\mu\to\nu) = \frac{1}{M}\,\frac{e^{-\beta E_n}}{\sum_{m=0}^{q-1} e^{-\beta E_m}},$$

with $M$ the number of spins, and acceptance $A(\mu\to\nu) = 1$ always.
Compare with standard Metropolis for the Potts model (generalization of the Ising one).

**Sub-questions**

- [ ] (a) Show that the heat bath transition probabilities satisfy detailed balance and ergodicity.
- [ ] (b) $q = 10$, $T = 0.5$, $20\times 20$ lattice, periodic BCs, random initial configuration: determine the equilibration time for heat bath and Metropolis by plotting the internal energy vs. iterations. (Optional: other sizes, $T$, $q$.)
- [ ] (c) Which algorithm converges fastest, and by how much?

## Relevant topics

- Heat bath algorithm — [§2.9, p. 19](../../Coursenotes/monte_carlo_2025.pdf#page=19)
- Detailed balance, ergodicity — [§2.2–2.3, p. 9](../../Coursenotes/monte_carlo_2025.pdf#page=9)
- Equilibration — [§2.5, p. 11](../../Coursenotes/monte_carlo_2025.pdf#page=11)
- Potts model and Ising mapping — [App. A, p. 49–50](../../Coursenotes/monte_carlo_2025.pdf#page=49)

## Course material

- Problem statement: [notes p. 41](../../Coursenotes/monte_carlo_2025.pdf#page=41)

## Deliverables for the report

- Proof for (a).
- $E(t)$ per spin vs. sweeps for both algorithms (several runs / averaged), with $\tau_{eq}$ indicated; quantitative speed-up (in sweeps *and* CPU time).

## Implementation notes

- Local energies only depend on the number of neighbours with each value ($0$–$4$): precompute Boltzmann factors.
- Metropolis for Potts: propose a new value uniformly among the other $q-1$ values.
- For $q=10$, the transition at $T_c = 1/\ln(1+\sqrt{q})\approx 0.70$ is first order; $T=0.5$ is in the ordered phase.

## Possible exam questions

- Why is heat bath more efficient than Metropolis for large $q$?
- Is heat bath for $q=2$ the same as Metropolis? (Glauber dynamics)

## Results & notes

_To be filled in._

## AI usage log

_To be filled in._
