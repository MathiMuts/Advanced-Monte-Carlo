# 4.13 — Monte Carlo in continuous time for a persistent random walk

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| ✅ yes | analytical + simulation | [p. 47](../../Coursenotes/monte_carlo_2025.pdf#page=47) | ⬜ todo |

## Question

A 1D random walker on the integers starts at $x = 0$. At each time step ($\Delta t = 1$) it
stays with probability $P(x\to x) = 1-2\varepsilon$ or jumps to $x\pm 1$ with probability
$\varepsilon$ each. Take $\varepsilon = 0.01$: the walker mostly stays put.

**Continuous-time algorithm:** first compute analytically $\langle\Delta t\rangle$, the
average time spent on a site; then at every step jump left or right with equal probability
and update $t \to t + \Delta t$ (no wasted "stay" steps).

**Sub-questions**

- [ ] (0) Compute $\langle \Delta t\rangle$ (and the waiting-time distribution) analytically.
- [ ] (a) Starting at $x = 0$, compute the time to reach $x = 20$ for the first time, averaged over many simulations. Compare brute-force simulation with the continuous-time algorithm.
- [ ] (b) What is the difference in run time of the two codes to reach $t = 10^6\,\Delta t$?

## Relevant topics

- Monte Carlo in continuous time (BKL / n-fold way) — [§2.11.3, p. 24](../../Coursenotes/monte_carlo_2025.pdf#page=24)
- Geometric vs. exponential waiting times
- First-passage times of random walks (heavy-tailed distribution — careful with averages!)

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

- Derivation of $\langle\Delta t\rangle = 1/(2\varepsilon)$ and the waiting-time distribution.
- Distribution (histogram, log scale) and mean of first-passage times from both methods; state number of runs.
- CPU-time comparison for reaching $t = 10^6$.

## Implementation notes

- Exact equivalence: draw the waiting time from the geometric distribution with $p = 2\varepsilon$ (or exponential approximation); discuss which one you use.
- The 1D first-passage time has infinite mean for an unbounded walk — expect a very broad distribution; consider a cap / report median too, and discuss.

## Possible exam questions

- When is continuous-time MC advantageous? Does it change the physics/statistics?
- How would you generalize it to the Ising model at low $T$?

## Results & notes

_To be filled in._
