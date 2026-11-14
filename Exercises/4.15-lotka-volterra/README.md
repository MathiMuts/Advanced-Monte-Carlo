# 4.15 — Lotka–Volterra model

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| ✅ yes | simulation | [p. 48](../../Coursenotes/monte_carlo_2025.pdf#page=48) | ⬜ todo |

## Question

Predator–prey dynamics with prey $Y_1$ and predator $Y_2$ (populations $X_1$, $X_2$):

$$Y_1 \xrightarrow{k_1} 2Y_1, \qquad Y_1 + Y_2 \xrightarrow{k_2} 2Y_2, \qquad Y_2 \xrightarrow{k_3} \emptyset,$$

with $k_1 = 1$, $k_2 = 0.005$, $k_3 = 0.6$, initial state 100 prey and 20 predators.

**Sub-questions**

- [ ] (a) With Gillespie, plot the trajectory in the $(X_1, X_2)$ plane and $X_1(t)$, $X_2(t)$ vs. time.
- [ ] (b) Estimate the average number of oscillations before reaching one of the two absorbing states ($X_1 = X_2 = 0$, or $X_1\to\infty$, $X_2 = 0$).
- [ ] (c) How often does the system end in $X_1 = X_2 = 0$ compared to $X_1\to\infty$, $X_2 = 0$?
- [ ] (d) Distribution of extinction times (time to reach $X_1 = 0$ or $X_2 = 0$).

## Relevant topics

- Coupled chemical reactions, rate equations — [§3.1, p. 27](../../Coursenotes/monte_carlo_2025.pdf#page=27)
- Gillespie algorithm — [§3.1.2, p. 29](../../Coursenotes/monte_carlo_2025.pdf#page=29)
- Deterministic Lotka–Volterra: fixed point $(k_3/k_2,\ k_1/k_2) = (120, 200)$, neutral cycles; stochastic noise drives the system to absorbing states

## Course material

- Problem statement: [notes p. 48](../../Coursenotes/monte_carlo_2025.pdf#page=48)
- Gillespie, J. Phys. Chem. 81, 2340 (1977): <http://www.caam.rice.edu/~cox/gillespie.pdf>

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

- Phase-plane trajectory (with deterministic orbit/fixed point for comparison) and time series.
- Histogram of the number of oscillations, with a clearly stated definition of "one oscillation".
- Fraction of runs ending in each absorbing state (with binomial error).
- Histogram of extinction times; number of runs.

## Implementation notes

- Propensities: $a_1 = k_1X_1$, $a_2 = k_2X_1X_2$, $a_3 = k_3X_2$.
- Once $X_2 = 0$ the prey grow exponentially: stop the run there (it is absorbing for the predators) and classify the outcome.
- Count oscillations e.g. by counting crossings of $X_1$ through the fixed-point value, or by the winding angle around the fixed point.

## Possible exam questions

- Why does the stochastic model always go extinct while the deterministic one oscillates forever?
- What is conserved in the deterministic Lotka–Volterra model?

## Results & notes

_To be filled in._

## AI usage log

_To be filled in._
