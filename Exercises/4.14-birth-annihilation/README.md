# 4.14 — Birth–annihilation process

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| ✅ yes | analytical + simulation | [p. 47](../../Coursenotes/monte_carlo_2025.pdf#page=47) | ⬜ todo |

## Question

A single particle species evolves through

$$A \xrightarrow{\lambda} \emptyset, \qquad A \xrightarrow{\mu} AA,$$

with rates $\lambda$ (annihilation) and $\mu$ (birth).

**Sub-questions**

- [ ] (a) Write down and solve the deterministic differential equation for the average number of particles.
- [ ] (b) Simulate with the Gillespie algorithm starting from $N = 10\,000$ and $N = 100$ particles, with $\lambda = 1$, $\mu = 0.2$. Compare with the deterministic solution.
- [ ] (c) Starting from $N = 100$, $\lambda = 1$, $\mu = 0.2$: histogram of extinction times (time until all particles are gone), from many repeated simulations.

## Relevant topics

- Coupled chemical reactions — [§3.1, p. 27](../../Coursenotes/monte_carlo_2025.pdf#page=27)
- Rate equations — [§3.1.1, p. 29](../../Coursenotes/monte_carlo_2025.pdf#page=29)
- Gillespie algorithm — [§3.1.2, p. 29](../../Coursenotes/monte_carlo_2025.pdf#page=29)
- Master equation — [App. B, p. 50](../../Coursenotes/monte_carlo_2025.pdf#page=50)
- Fluctuations $\sim\sqrt N$, absorbing states

## Course material

- Problem statement: [notes p. 47](../../Coursenotes/monte_carlo_2025.pdf#page=47)

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

- Solution $\langle N(t)\rangle = N_0 e^{-(\lambda-\mu)t}$ with derivation.
- Several stochastic trajectories vs. the deterministic curve, for $N_0 = 10^4$ and $N_0 = 100$ (log scale helps); relative fluctuations.
- Histogram of extinction times (number of runs, bins), mean and spread.

## Implementation notes

- Propensities: $a_1 = \lambda N$, $a_2 = \mu N$; total $a_0 = (\lambda+\mu)N$. Waiting time $\tau = -\ln(u_1)/a_0$; choose reaction with $u_2$.
- Optional cross-check: the extinction time distribution can be obtained analytically (generating functions) or compared to the deterministic estimate $\ln N_0/(\lambda-\mu)$.

## Possible exam questions

- Derive the Gillespie algorithm: why is the waiting time exponential?
- Why does the deterministic equation never predict extinction?

## Results & notes

_To be filled in._

## AI usage log

_To be filled in._
