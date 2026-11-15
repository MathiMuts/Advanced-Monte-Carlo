# 4.2 — Gaussian RNG (Box–Muller)

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| ✅ yes | simulation | [p. 32–33](../../Coursenotes/monte_carlo_2025.pdf#page=32) | ✅ done (in report) |

## Question

Two independent standard Gaussian numbers $x, y$ have joint density

$$f(x,y)\,dx\,dy = \frac{1}{2\pi}\exp\!\left(-\frac{x^2+y^2}{2}\right)dx\,dy ,$$

which in polar coordinates becomes

$$f(r,\theta)\,dr\,d\theta = \frac{1}{2\pi}\exp\!\left(-\frac{r^2}{2}\right) r\,dr\,d\theta .$$

Draw $\theta \sim U[0, 2\pi]$ and $r$ by inverting the CDF
$F(r) = \int_0^r e^{-z^2/2} z\,dz$, then transform back to $(x, y)$.

**Sub-questions**

- [x] (a) Program the algorithm and show that it generates pairs of normally distributed random variables.
- [x] (b) How must the algorithm be adapted to obtain Gaussian numbers with mean $\mu$ and variance $\sigma^2$?

## Relevant topics

- Inverse transform sampling (see [4.1](../4.01-non-uniform-random-numbers/)) — [Ch. 1, p. 3](../../Coursenotes/monte_carlo_2025.pdf#page=3)
- Change of variables in 2D, Box–Muller transform
- Testing normality and independence (histograms, Q–Q plot, moments, correlation $\langle xy\rangle$)

## Course material

- Problem statement: [notes p. 32](../../Coursenotes/monte_carlo_2025.pdf#page=32)
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

- Histograms of $x$ and $y$ with the exact $\mathcal N(0,1)$ density overlaid; sample mean/variance.
- 2D histogram / scatter of $(x,y)$ and a check of independence (e.g. correlation coefficient).
- Short derivation of $F(r) = 1 - e^{-r^2/2}$ and $r = \sqrt{-2\ln(1-u)}$; answer to (b).

## Implementation notes

- $1-u$ and $u$ are equally distributed; avoid $\ln 0$.
- Compare speed/result with `rng.standard_normal` as a sanity check.

## Possible exam questions

- Why go to polar coordinates instead of inverting the 1D Gaussian CDF?
- Why are the two outputs independent?

## Results & notes

All runs: $N = 100\,000$ pairs, `SEED = 1` (`np.random.default_rng`).

### Derivation

The radial density is $p(r) = r\,e^{-r^2/2}$ on $[0,\infty)$, so

$$F(r) = \int_0^r e^{-z^2/2} z\,dz = 1 - e^{-r^2/2}
\quad\Rightarrow\quad r = F^{-1}(u_1) = \sqrt{-2\ln(1-u_1)} ,$$

and $\theta = 2\pi u_2$. Then $x = r\cos\theta$, $y = r\sin\theta$.
The joint density factorises, $f(r,\theta) = \underbrace{r e^{-r^2/2}}_{r}\cdot\underbrace{\tfrac{1}{2\pi}}_{\theta}$,
so $r$ and $\theta$ must be drawn from **two independent** uniforms $u_1, u_2$.
Going back to Cartesian coordinates the density factorises again,
$\frac{1}{2\pi}e^{-(x^2+y^2)/2} = \phi(x)\,\phi(y)$, so $x$ and $y$ are independent $\mathcal N(0,1)$.

### (a) Pairs of normal random numbers

| | mean | variance |
|---|---|---|
| $x$ | $-0.0033 \pm 0.0032$ | $0.9954$ |
| $y$ | $+0.0072 \pm 0.0032$ | $1.0036$ |

- Histograms of $x$ and $y$ follow the exact $\mathcal N(0,1)$ density
  ([`box_muller_hist`](figures/box_muller_hist.png)).
- The scatter plot of $(x,y)$ is a circularly symmetric cloud
  ([`box_muller_xy`](figures/box_muller_xy.png)).
- Correlation $\rho_{xy} = -0.0016$, compatible with $0 \pm 1/\sqrt N = 0 \pm 0.0032$.
  ($\rho = 0$ alone does not prove independence; the factorisation above does.)
- The mean of $y$ is $2.2$ standard errors from 0: a normal fluctuation for one seed.

**Bug found:** using the same `u` for $r$ and $\theta$ makes $r$ a function of $\theta$,
so all points lie on a spiral instead of a 2D Gaussian.

### (b) Mean $\mu$ and variance $\sigma^2$

Keep the algorithm and rescale the output: $x' = \mu + \sigma x$, $y' = \mu + \sigma y$.
Then $\langle x'\rangle = \mu$, $\mathrm{Var}(x') = \sigma^2$, and $x'$ is still Gaussian
(a linear change of variables, $dx = dx'/\sigma$, gives
$\frac{1}{\sqrt{2\pi\sigma^2}}e^{-(x'-\mu)^2/2\sigma^2}$).
Equivalently, take $r = \sigma\sqrt{-2\ln(1-u_1)}$ and shift by $\mu$.

With $\mu = 3$, $\sigma = 2$
([`box_muller_hist_mu_sigma`](figures/box_muller_hist_mu_sigma.png),
[`box_muller_xy_mu_sigma`](figures/box_muller_xy_mu_sigma.png)):

| | mean (expected 3) | variance (expected 4) |
|---|---|---|
| $x'$ | $2.9934 \pm 0.0063$ | $3.9814$ |
| $y'$ | $3.0145 \pm 0.0063$ | $4.0142$ |

Different parameters per axis, $\mu = (3, -5)$, $\sigma = (2, 1)$, give an ellipse elongated along $x$
([`box_muller_hist_mu_sigma_asym`](figures/box_muller_hist_mu_sigma_asym.png),
[`box_muller_xy_mu_sigma_asym`](figures/box_muller_xy_mu_sigma_asym.png)):

| | mean | variance |
|---|---|---|
| $x'$ | $2.9934 \pm 0.0063$ (expected 3) | $3.9814$ (expected 4) |
| $y'$ | $-4.9928 \pm 0.0032$ (expected $-5$) | $1.0036$ (expected 1) |

The rescaled samples are the same Box–Muller pairs, so their relative deviations are those of (a).

### Answers to the exam questions

- *Why polar coordinates?* The 1D Gaussian CDF (error function) has no closed-form inverse.
  In 2D the Jacobian $r$ makes $r e^{-r^2/2}$ integrable in closed form, so $F^{-1}$ is explicit.
- *Why are $x$ and $y$ independent?* Their joint density $\phi(x)\phi(y)$ factorises, which follows
  from $r$ and $\theta$ being independent ($u_1$, $u_2$ independent).
