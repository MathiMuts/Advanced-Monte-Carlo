# 4.2 — Gaussian RNG (Box–Muller)

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| ✅ yes | simulation | [p. 32–33](../../Coursenotes/monte_carlo_2025.pdf#page=32) | ⬜ todo |

## Question

Two independent standard Gaussian numbers $x, y$ have joint density

$$f(x,y)\,dx\,dy = \frac{1}{2\pi}\exp\!\left(-\frac{x^2+y^2}{2}\right)dx\,dy ,$$

which in polar coordinates becomes

$$f(r,\theta)\,dr\,d\theta = \frac{1}{2\pi}\exp\!\left(-\frac{r^2}{2}\right) r\,dr\,d\theta .$$

Draw $\theta \sim U[0, 2\pi]$ and $r$ by inverting the CDF
$F(r) = \int_0^r e^{-z^2/2} z\,dz$, then transform back to $(x, y)$.

**Sub-questions**

- [ ] (a) Program the algorithm and show that it generates pairs of normally distributed random variables.
- [ ] (b) How must the algorithm be adapted to obtain Gaussian numbers with mean $\mu$ and variance $\sigma^2$?

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

_To be filled in._
