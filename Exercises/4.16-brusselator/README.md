# 4.16 — Brusselator

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| ✅ yes | simulation | [p. 48](../../Coursenotes/monte_carlo_2025.pdf#page=48) | ⬜ todo |

## Question

Autocatalytic reaction model (Brusselator):

$$\emptyset \xrightarrow{k_1} Y_1, \qquad Y_1 \xrightarrow{k_2} Y_2, \qquad 2Y_1 + Y_2 \xrightarrow{k_3} 3Y_1, \qquad Y_1 \xrightarrow{k_4} \emptyset,$$

with rates as in Gillespie's original paper: $k_1 = 5\times 10^3$, $k_2 = 50$,
$k_3 = 5\times10^{-5}$, $k_4 = 5$.

**Sub-questions**

- [ ] (a) With Gillespie, plot the trajectory in the $X_1$–$X_2$ plane and $X_1(t)$, $X_2(t)$ for $X_1(0) = 1000$, $X_2(0) = 2000$.
- [ ] (b) Repeat for (a) $X_1(0) = 1000, X_2(0) = 4000$; (b) $X_1(0) = 5000, X_2(0) = 5000$; (c) $X_1(0) = 500, X_2(0) = 500$. Show that the system approaches a limit-cycle oscillation. Compare with Fig. 15 of Gillespie's paper.

## Relevant topics

- Coupled chemical reactions, rate equations — [§3.1, p. 27](../../Coursenotes/monte_carlo_2025.pdf#page=27)
- Gillespie algorithm — [§3.1.2, p. 29](../../Coursenotes/monte_carlo_2025.pdf#page=29)
- Limit cycles, Hopf bifurcation (contrast with the neutral cycles of [4.15](../4.15-lotka-volterra/))

## Course material

- Problem statement: [notes p. 48](../../Coursenotes/monte_carlo_2025.pdf#page=48)
- Gillespie, J. Phys. Chem. 81, 2340 (1977), Eqs. 44(a–d) and Fig. 15: <http://www.caam.rice.edu/~cox/gillespie.pdf> (note: slightly different notation)

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

- Phase-plane plots for the four initial conditions (ideally in one figure, all converging to the same cycle), plus time series.
- Comparison with the deterministic rate equations (ODE solution) and with Gillespie's Fig. 15.

## Implementation notes

- Propensities: $a_1 = k_1$, $a_2 = k_2X_1$, $a_3 = \tfrac{k_3}{2}X_1(X_1-1)X_2$ (check the combinatorial convention used in the notes/paper!), $a_4 = k_4X_1$.
- Many events per unit time ($\sim 10^5$–$10^6$): use `numba` or store only every $n$-th state.

## Possible exam questions

- Why is a limit cycle robust to noise, unlike Lotka–Volterra orbits?
- How do the propensity functions follow from the reaction stoichiometry?

## Results & notes

_To be filled in._

## AI usage log

_To be filled in._
