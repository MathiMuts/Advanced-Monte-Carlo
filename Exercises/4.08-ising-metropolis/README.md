# 4.8 — Metropolis algorithm for the Ising model

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| ✅ yes | simulation | [p. 39–41](../../Coursenotes/monte_carlo_2025.pdf#page=39) | ⬜ todo |

## Question

Single-spin-flip Metropolis on an $N\times N$ Ising lattice with periodic boundaries,
starting from a random configuration:

1. Pick a spin $s_i$ at random.
2. Compute $\Delta E = E_\text{fin} - E_\text{in}$ for flipping $s_i\to -s_i$.
3. Flip if $\Delta E \le 0$, or if $r \le \exp(-\Delta E/k_BT)$ with $r\sim U[0,1]$.
4. Repeat ($\sim 10^6$–$10^8$ steps). One **sweep** = $N^2$ attempted steps.

Observables: magnetization per spin $m = \frac{1}{N^2}\sum_i s_i$, energy, and the
time autocorrelation

$$\chi(t) = \frac{1}{t_f}\sum_{s=\tau_{eq}}^{\tau_{eq}+t_f}\big[m(s)-\langle m\rangle\big]\big[m(s+t)-\langle m\rangle\big] \sim e^{-t/\tau}.$$

Exact spontaneous magnetization: $m(T) = \left[1-\sinh^{-4}(2J/T)\right]^{1/8}$ for $T<T_c = 2/\ln(1+\sqrt2)\approx 2.269$.

**Sub-questions**

- [ ] (a) $T = 2$, $N = 50$: plot $m$ vs. MC time (cf. Fig. 3 of the notes) and compare $\langle m\rangle$ with the exact value.
- [ ] (b) Estimate the equilibration time $\tau_{eq}$ from the plot.
- [ ] (c) Energy histogram at $T = 2$ (sampling after $\tau_{eq}$); compare with the reweighting result of [4.7](../4.07-ising-uniform-sampling/).
- [ ] (d) $N = 50$, $T = 2.2$: compute $\chi(t)$ (per sweep), normalized by $\chi(0)$.
- [ ] (e) Determine the correlation time $\tau$ from $\chi(t)\sim e^{-t/\tau}$.
- [ ] (f) *Optional:* at $T = T_c$, compute $\tau$ for $N = 5, 10, 25$; show critical slowing down (growth with $N$, much larger than at $T=2$) and fit $\tau\sim N^z$ to estimate $z$.

## Relevant topics

- Metropolis algorithm — [§2.4, p. 10](../../Coursenotes/monte_carlo_2025.pdf#page=10)
- Equilibration — [§2.5, p. 11](../../Coursenotes/monte_carlo_2025.pdf#page=11) (Fig. 3)
- Correlation time, error estimation for correlated data — [§2.6, p. 12](../../Coursenotes/monte_carlo_2025.pdf#page=12)
- Critical slowing down, dynamical exponent $z$ — [§2.7, p. 16](../../Coursenotes/monte_carlo_2025.pdf#page=16)
- (Contrast: Wolff cluster algorithm — [§2.8, p. 17](../../Coursenotes/monte_carlo_2025.pdf#page=17))
- Ising model, exact results — [App. A, p. 49](../../Coursenotes/monte_carlo_2025.pdf#page=49)

## Course material

- Problem statement: [notes p. 39](../../Coursenotes/monte_carlo_2025.pdf#page=39)
- "Some interesting tricks" (precomputed exponentials, local $\Delta E$, temperature annealing): [p. 41](../../Coursenotes/monte_carlo_2025.pdf#page=41)

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

- $m(t)$ for a few independent runs at $T=2$, with the exact value as a horizontal line; $\tau_{eq}$ marked.
- Energy histogram at $T=2$ vs. reweighted histogram from 4.7.
- $\chi(t)/\chi(0)$ on a log scale with exponential fit and $\tau$ (with uncertainty).
- (Optional) $\tau$ vs. $N$ log–log at $T_c$ with fitted $z$ (literature $z\approx 2.17$ for Metropolis).

## Implementation notes

- Only $\Delta E \in \{-8,-4,0,4,8\}$ ($J=1$): precompute $e^{-\beta\Delta E}$ for $\Delta E>0$ (how many values? — asked in the notes).
- Use `numba` for the inner loop; measure once per sweep.
- At $T<T_c$ on a finite lattice $m$ can flip sign: use $|m|$ when comparing with the exact value.

## Possible exam questions

- Prove that the Metropolis acceptance satisfies detailed balance.
- Why does $\tau$ diverge at $T_c$ and how does Wolff solve it?
- How does $\tau$ enter the statistical error of $\langle m\rangle$?

## Results & notes

_To be filled in._

## AI usage log

_To be filled in._
