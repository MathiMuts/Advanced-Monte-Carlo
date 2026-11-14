# 4.6 — Detailed balance

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| ✅ yes | analytical | [p. 36](../../Coursenotes/monte_carlo_2025.pdf#page=36) | ⬜ todo |

## Question

A system has three states with energies $E_1 < E_2 < E_3$. The only allowed transitions
are $1\to 2$, $2\to 3$ and $3\to 1$ (a cycle), or staying in the same state.

**Sub-questions**

- [ ] (1) Assigning arbitrary rates to these transitions, write the $3\times 3$ stochastic matrix describing the process.
- [ ] (2) Does this dynamics satisfy detailed balance? Is it ergodic?
- [ ] (3) Show that the rates can be chosen such that the equilibrium distribution is Boltzmann, $p_i = e^{-\beta E_i}/Z$ with $Z = \sum_{i=1}^3 e^{-\beta E_i}$.

> Note from the notes: this is an example showing that detailed balance is **not a
> necessary** condition to obtain the Boltzmann distribution as equilibrium.

## Relevant topics

- Stochastic matrices and stationary vectors ([4.5](../4.05-stochastic-matrices/)) — [§2.1, p. 7](../../Coursenotes/monte_carlo_2025.pdf#page=7)
- Ergodicity — [§2.2, p. 9](../../Coursenotes/monte_carlo_2025.pdf#page=9)
- Detailed balance vs. global balance (stationarity) — [§2.3, p. 9](../../Coursenotes/monte_carlo_2025.pdf#page=9)

## Course material

- Problem statement: [notes p. 36](../../Coursenotes/monte_carlo_2025.pdf#page=36)

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

- The matrix, the argument for (2), and explicit rates for (3).
- Optional: numerical check — iterate $P^n w$ (or simulate the chain) and compare the stationary vector with $p_i$.

## Possible exam questions

- What is the difference between global balance and detailed balance?
- Why do most MC algorithms impose detailed balance anyway?
- What does a non-zero probability current in steady state mean physically?

## Results & notes

_To be filled in._

## AI usage log

_To be filled in._
