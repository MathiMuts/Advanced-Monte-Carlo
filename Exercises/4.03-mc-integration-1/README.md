# 4.3 — Monte Carlo integration (I): importance sampling

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| ✅ yes | analytical + simulation | [p. 33–34](../../Coursenotes/monte_carlo_2025.pdf#page=33) | ⬜ todo |

## Question

Estimate with Monte Carlo the integral

$$I = \int_{-\infty}^{\infty} \exp\!\left(-\frac{r^2}{2}\right)(x+y+z)^2\,dx\,dy\,dz, \qquad r^2 = x^2+y^2+z^2 ,$$

using the factor $e^{-r^2/2}$ as a density function on the domain (careful with the
normalization factor). The result is compared with the analytical value and with the
Metropolis approach of [4.4](../4.04-mc-integration-2-metropolis/).

**Sub-questions**

- [ ] (a) Compute $I$ analytically.
- [ ] (b) Use a Gaussian RNG to generate $x, y, z$ and estimate $I$; compare with the analytical result.
- [ ] (c) Compute the variance $\sigma^2$ of the estimate for different numbers of sampled points $N$, and show that $\sigma^2 \propto 1/N$.
- [ ] (d) Why can't we swap the two factors, i.e. use $(x+y+z)^2$ as density and $e^{-r^2/2}$ as integrand?

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

_To be filled in._

## AI usage log

_To be filled in._
