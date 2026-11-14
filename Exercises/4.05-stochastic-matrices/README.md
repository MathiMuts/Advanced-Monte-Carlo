# 4.5 — Stochastic matrices

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| ✅ yes | analytical (proofs) | [p. 35–36](../../Coursenotes/monte_carlo_2025.pdf#page=35) | ⬜ todo |

## Question

An $N\times N$ matrix $P$ is **stochastic** if (a) $P_{ij}\ge 0$ for all $i,j$ and
(b) every column sums to one: $\sum_{i=1}^N P_{ij} = 1\ \ \forall j$.
$P_{ij} = p(j\to i)$ is the transition probability from state $j$ to state $i$ in a time
step $\Delta t$, and a probability vector evolves as $w(t+\Delta t) = P\,w(t)$.
A *non-negative vector* has all entries $\ge 0$.

**Sub-questions**

- [ ] (a) Show that, starting from a non-negative vector $w$, $P$ generates non-negative vectors at all later times.
- [ ] (b) Show that the product of two stochastic matrices is stochastic.
- [ ] (c) With $\|w\|_1 = \sum_j |w_j|$ and an arbitrary (possibly negative) vector $y$, show that $\|Py\|_1 \le \|y\|_1$, and deduce that every eigenvalue satisfies $|\lambda|\le 1$.
- [ ] (d) Show that a stochastic matrix has at least one eigenvalue $\lambda = 1$. (Hint: a suitable *left* eigenvector.)

## Relevant topics

- Markov chains and the transition matrix — [§2.1, p. 7](../../Coursenotes/monte_carlo_2025.pdf#page=7)
- Ergodicity, stationary distribution, Perron–Frobenius — [§2.2, p. 9](../../Coursenotes/monte_carlo_2025.pdf#page=9)
- Master equation (continuous-time limit) — [App. B, p. 50](../../Coursenotes/monte_carlo_2025.pdf#page=50)

## Course material

- Problem statement: [notes p. 35](../../Coursenotes/monte_carlo_2025.pdf#page=35)
- Note: §2.1 states a proposition "proven during the exercise session" — this exercise.

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

- Clean written proofs of (a)–(d). Optionally a numerical illustration (random stochastic matrix, its spectrum in the complex plane inside the unit circle, convergence of $P^n w$).

## Possible exam questions

- Why does $\lambda=1$ correspond to the stationary distribution? Why is it unique for an ergodic chain?
- What determines the speed of convergence to equilibrium (second-largest eigenvalue)?

## Results & notes

_To be filled in._
