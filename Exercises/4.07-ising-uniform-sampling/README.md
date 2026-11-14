# 4.7 — Ising model: uniform sampling

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| ✅ yes | simulation | [p. 36–39](../../Coursenotes/monte_carlo_2025.pdf#page=36) | ⬜ todo |

## Question

2D Ising model on an $N\times N$ square lattice with periodic boundary conditions,
$s_i = \pm 1$, energy $E = -J\sum_{\langle ij\rangle} s_i s_j$ with $J = 1$ (nearest neighbours).
Energy per bond $e = E/2N^2 \in [-1, 1]$. The aim is to show that sampling all
configurations uniformly is very inefficient.

- **Uniform sampling:** repeatedly generate a random configuration, compute $E$, store/histogram it.
- **Boltzmann sampling with hit-and-miss:** generate a random configuration, compute $E$,
  draw $r\sim U[0,1]$, keep $E$ if $r \le \exp(-\beta(E-E_0))$ with $E_0 = -2N^2$ the ground-state energy.
  At $\beta = 0$ this reduces to uniform sampling.
- **Reweighting:** from the uniform histogram $P(E)$, obtain $P_T(E) \propto e^{-E/T}P(E)$.

**Sub-questions**

- [ ] (0) Which configuration has $e = +1$? (asked in the text)
- [ ] (a) For $N = 16$, histogram $e$ with uniform sampling ($10^4$–$10^5$ samples).
- [ ] (b) Hit-and-miss at $T = 10^5,\ 10^3,\ 10^2,\ 10$ ($k_B = 1$): fraction of hits over the total number of generated configurations for each $T$. Conclude that hit-and-miss performs very poorly.
- [ ] (c) Reweighting: plot $P_T(E)$ for $T = 10^5,\ 10^3,\ 10,\ 2$. Is this a reasonable method? (Compare later with Metropolis in [4.8](../4.08-ising-metropolis/).)

## Relevant topics

- Why simple sampling fails: the Boltzmann weight concentrates on an exponentially small part of configuration space — [Ch. 2 intro, p. 6](../../Coursenotes/monte_carlo_2025.pdf#page=6)
- Ising model, ground states, $T_c$ — [App. A, p. 49](../../Coursenotes/monte_carlo_2025.pdf#page=49)
- Hit-and-miss ([4.1](../4.01-non-uniform-random-numbers/)), histogram reweighting
- Periodic boundary conditions (careful with `mod` of negative numbers)

## Course material

- Problem statement: [notes p. 36](../../Coursenotes/monte_carlo_2025.pdf#page=36)
- Fig. 13 (periodic boundary conditions): [p. 38](../../Coursenotes/monte_carlo_2025.pdf#page=38)

## Files

| File | Content |
|---|---|
| [`functions.py`](functions.py) | Long functions: samplers, simulations, analysis and plotting helpers (`save_figure`, `KUL_BLUES`). |
| [`code.ipynb`](code.ipynb) | Runs the functions: parameters, data, figures and numbers for the report, one section per sub-question. |
| [`figures/`](figures/) | Saved plots (`.png` + `.pdf`) used in the report. |

The module is called `functions.py` and not `code.py`, because a `code.py` would hide
Python's built-in `code` module, which IPython/Jupyter need. Thanks to
`%autoreload 2`, edits to `functions.py` are picked up by the notebook without a kernel restart.

## Deliverables for the report

- Histogram of $e$ from uniform sampling (state $N$, number of samples, bins); compare with a Gaussian of width $\sim 1/N$.
- Table of hit fractions vs. $T$.
- Reweighted histograms for the four temperatures, and a discussion of where they become unreliable (no samples at low $E$).

## Implementation notes

- Vectorize: energy via `np.roll` on the whole lattice; generate many configurations at once.
- For reweighting, work in log space ($\log P + (-E/T)$, subtract the max) to avoid overflow.

## Possible exam questions

- Why is uniform sampling hopeless at low $T$? Estimate the probability of hitting the ground state.
- When does reweighting work, and why does it fail at $T=2$?

## Results & notes

_To be filled in._

## AI usage log

_To be filled in._
