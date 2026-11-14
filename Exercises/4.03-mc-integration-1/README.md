# 4.3 — Monte Carlo integration (I): importance sampling

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| ✅ yes | analytical + simulation | [p. 33–34](../../Coursenotes/monte_carlo_2025.pdf#page=33) | 🟨 code done, report todo |

## Question

Estimate with Monte Carlo the integral

$$I = \int_{-\infty}^{\infty} \exp\!\left(-\frac{r^2}{2}\right)(x+y+z)^2\,dx\,dy\,dz, \qquad r^2 = x^2+y^2+z^2 ,$$

using the factor $e^{-r^2/2}$ as a density function on the domain (careful with the
normalization factor). The result is compared with the analytical value and with the
Metropolis approach of [4.4](../4.04-mc-integration-2-metropolis/).

**Sub-questions**

- [x] (a) Compute $I$ analytically.
- [x] (b) Use a Gaussian RNG to generate $x, y, z$ and estimate $I$; compare with the analytical result.
- [x] (c) Compute the variance $\sigma^2$ of the estimate for different numbers of sampled points $N$, and show that $\sigma^2 \propto 1/N$.
- [x] (d) Why can't we swap the two factors, i.e. use $(x+y+z)^2$ as density and $e^{-r^2/2}$ as integrand?

## Relevant topics

- Monte Carlo integration, importance sampling, variance of the estimator — [Ch. 1, p. 3–6](../../Coursenotes/monte_carlo_2025.pdf#page=3)
- Central limit theorem, $1/\sqrt N$ convergence
- Gaussian random numbers ([4.2](../4.02-gaussian-rng/))

## Course material

- Problem statement: [notes p. 33](../../Coursenotes/monte_carlo_2025.pdf#page=33)
- Theory: [Ch. 1, p. 3](../../Coursenotes/monte_carlo_2025.pdf#page=3)

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

- Analytical derivation of $I$.
- Table/plot of the MC estimate with error bars vs. $N$, converging to the exact value.
- Log–log plot of $\sigma^2$ vs. $N$ with a fitted slope $\approx -1$ (variance from many independent runs at each $N$).
- Argument for (d).

## Implementation notes

- Normalization: $e^{-r^2/2} = (2\pi)^{3/2}\, w(\mathbf r)$ with $w$ the standard 3D Gaussian density, so $I = (2\pi)^{3/2}\,\langle (x+y+z)^2\rangle_w$.
- Hint for (d): a density must be normalizable and non-negative on the domain — check both.

## Possible exam questions

- What is the error of a MC integral estimate, and how does it scale with $N$ and dimension?
- What makes a good importance-sampling density?

## Results & notes

All runs: `SEED = 1` (`np.random.default_rng`), Gaussian numbers from `scipy.stats.norm.rvs`.

### (a) Analytical value

$(x+y+z)^2 = x^2+y^2+z^2 + 2(xy+yz+zx)$. The cross terms are odd in one coordinate and vanish.
Each square term gives $\int x^2 e^{-x^2/2}dx \cdot (\sqrt{2\pi})^2 = (2\pi)^{3/2}\langle x^2\rangle = (2\pi)^{3/2}$, so

$$I = 3\,(2\pi)^{3/2} = 6\sqrt2\,\pi^{3/2} \approx 47.249 .$$

Computed in the notebook with `sympy` (symbolic triple integral over $\mathbb R^3$).

### (b) Importance-sampling estimate

$e^{-r^2/2} = (2\pi)^{3/2}\,w(\mathbf r)$, so $I = (2\pi)^{3/2}\langle f\rangle_w$ with $f = (x+y+z)^2$.
The standard error is $(2\pi)^{3/2}\,s_f/\sqrt N$, with $s_f$ the sample standard deviation (`ddof=1`).

With $N = 10^6$ points: $I_\text{MC} = 47.241 \pm 0.067$, which is $-0.12$ standard errors from the exact value.

### (c) Variance $\propto 1/N$

1000 independent runs at each of 13 values $N = 10 \dots 10^5$ (log-spaced)
([`mc_variance`](figures/mc_variance.png)). The error bar on each variance is $\sigma^2\sqrt{2/(M-1)}$, with $M = 1000$.

- Weighted fit of $\log\sigma^2$ vs $\log N$: $\sigma^2(I_N) = 4441\,N^{-1.000 \pm 0.004}$.
- Prediction: $\sigma^2(I_N) = (2\pi)^3\,\mathrm{Var}(f)/N = 18\,(2\pi)^3/N = 4465/N$.
  Here $s = x+y+z \sim \mathcal N(0,3)$ and $s^2/3 \sim \chi^2_1$, so $\mathrm{Var}(s^2) = 9 \cdot 2 = 18$.
- $N\sigma^2$ lies between 4067 and 4750 for all $N$ (each $\pm$ about 200).
- The variance of the sampled values $f_i$ does not shrink with $N$; only the variance of their mean does.

### (d) Why the two factors cannot be swapped

- $(x+y+z)^2 \ge 0$, but $\int_{\mathbb R^3}(x+y+z)^2\,d^3r = \infty$: it cannot be normalized, so it is not a probability density.
- On a finite box $[-L,L]^3$ it can be normalized, with $Z = (2L)^3L^2 \propto L^5$, and $I_\text{box} = Z\,\langle e^{-r^2/2}\rangle_p$.
  Points are drawn by rejection sampling (uniform proposal, acceptance $s^2/(3L)^2$), $10^6$ points per $L$
  ([`mc_swapped`](figures/mc_swapped.png)).

| $L$ | $I_\text{box}$ | $\sigma_g/\langle g\rangle$ |
|---|---|---|
| 1 | $4.376 \pm 0.001$ | 0.24 |
| 2 | $31.79 \pm 0.03$ | 1.00 |
| 4 | $47.47 \pm 0.26$ | 5.44 |
| 8 | $46.4 \pm 1.4$ | 30.2 |
| 16 | $44.8 \pm 7.4$ | 166 |

- A small box is biased (it cuts off the tails); a large box is unbiased but noisy.
  The relative spread per point grows as $L^{5/2}$, against $\sqrt{18}/3 = 1.41$ for the Gaussian density.
- The reason: the density puts most points at large $|x+y+z|$, where $e^{-r^2/2} \approx 0$.
  A good importance-sampling density follows the shape of |integrand|, so the ratio integrand/density is nearly constant.

### Answers to the exam questions

- *Error of a MC integral?* $\sigma_f/\sqrt N$ for independent samples, whatever the dimension; only the prefactor $\sigma_f$
  depends on the problem and on the chosen density.
- *Good importance-sampling density?* Non-negative, normalizable, easy to sample, and close in shape to |integrand|.
