# 4.11 — Kawasaki algorithm: non-local version

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| 🔶 at least one of 4.9 / 4.10 / 4.11 | simulation | [p. 43–44](../../Coursenotes/monte_carlo_2025.pdf#page=43) | ⬜ todo |

## Question

Same conserved-magnetization Ising model as [4.10](../4.10-kawasaki-local/), but with
**non-local** swaps of non-neighbouring spins. Keep two lists with the indices of the plus
spins $u = (1,2,3,5,7,10,\dots)$ and minus spins $d = (4,6,8,9,\dots)$, plus the spin
configuration $v$ of length $L_x L_y$. Pick a random $u_i$ and a random $d_j$, compute
$\Delta E$ for swapping them, and accept with the Metropolis rule. On acceptance:
$u_i' = d_j$, $d_j' = u_i$, $v'(u_i) = -v(u_i)$, $v'(d_j) = -v(d_j)$.

**Sub-questions**

- [ ] (a) Starting from Fig. 14(a), estimate $N_{acc}/N$ at $T = 0.5\,T_c$, $1.2\,T_c$, $2.5\,T_c$. Higher or lower than for the local algorithm?
- [ ] (b) Equilibration time at $T = 0.9\,T_c$; compare with [4.10](../4.10-kawasaki-local/).
- [ ] (c) Initial condition Fig. 14(b) — a $50\times 50$ square of plus spins surrounded by minus — at $T = 0.25\,T_c$ and $0.5\,T_c$: compare the shape evolution of the square (snapshots at selected times).
- [ ] (d) $T = 0.8\,T_c$, initial squares of size $10\times10$, $20\times20$, $30\times30$: show that the smallest square dissolves quickly while the largest persists for a long time.

## Relevant topics

- Conserved order parameter Ising model — [§2.10, p. 21](../../Coursenotes/monte_carlo_2025.pdf#page=21)
- Metropolis, equilibration — [§2.4–2.5, p. 10](../../Coursenotes/monte_carlo_2025.pdf#page=10)
- Nucleation, critical droplet size, surface tension; Ostwald ripening

## Course material

- Problem statement: [notes p. 43](../../Coursenotes/monte_carlo_2025.pdf#page=43), Fig. 14 on [p. 43](../../Coursenotes/monte_carlo_2025.pdf#page=43)
- Builds on [4.10](../4.10-kawasaki-local/) (same lattice and boundary conditions: $200\times 50$, fixed in $y$, periodic in $x$)

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

- $N_{acc}/N$ table vs. the local version.
- $e(t)$ at $0.9\,T_c$, local vs. non-local.
- Snapshot grids of the droplet at different times for (c) and (d).

## Implementation notes

- If the two chosen spins are neighbours, their mutual bond must be handled correctly in $\Delta E$.
- For (c)/(d) the lattice must be large enough to contain the square plus surroundings; state the lattice size used.

## Possible exam questions

- Does the non-local dynamics still satisfy detailed balance? Is the dynamics physical?
- Why do small droplets dissolve and large ones survive?

## Results & notes

_To be filled in._

## AI usage log

_To be filled in._
