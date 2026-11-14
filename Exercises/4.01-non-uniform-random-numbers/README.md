# 4.1 — Non-uniform random numbers

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| ✅ yes | simulation (+ short proof) | [p. 31–32](../../Coursenotes/monte_carlo_2025.pdf#page=31) | 🟨 in progress |

## Question

Generate random numbers with a given probability density $f(x)$ ($f\ge 0$, $\int f = 1$)
from uniform random numbers in $[0,1]$, using two methods:

- **Inverse CDF:** with $F(x) = \int_{-\infty}^{x} f(y)\,dy$, if $x_i \sim U[0,1]$ then
  $y_i = F^{-1}(x_i)$ is distributed with density $f$ (show this — "easy and left to you").
  Requires $F$ to be analytic and invertible.
- **Hit-and-miss:** for $f$ supported on $[a,b]$ with $M > f(x)$, draw $t\sim U[a,b]$,
  $s\sim U[0,M]$; keep $t$ if $s \le f(t)$ (hit), discard otherwise (miss).

**Sub-questions**

- [x] (0) Prove that $y = F^{-1}(x)$ with $x\sim U[0,1]$ has density $f$.
- [x] (a) Inverse CDF — generate and histogram numbers distributed
  - [x] uniformly in $[-2, 1]$
  - [x] exponentially on $\mathbb{R}^+$: $f(x) = e^{-x}$ for $x\ge 0$
  - [x] linearly on $[-1,1]$: $f(x) = (x+1)/2$
- [x] (b) Hit-and-miss — generate and histogram numbers distributed
  - [x] linearly on $[-1,1]$: $f(x) = (x+1)/2$
  - [x] $f(x) = -x(1-x)\,e^{-x^2}\log(1-x)$ on $[0,1]$
- [x] (c) Hit-and-miss: points uniformly distributed inside a circle of radius $R=1$.
- [x] (d) Same uniform disk *without* hit-and-miss, using an appropriate density $f(r,\theta)$ in polar coordinates.

## Relevant topics

- Inverse transform sampling, cumulative distribution function — [Ch. 1, p. 3](../../Coursenotes/monte_carlo_2025.pdf#page=3)
- Rejection (hit-and-miss) sampling and its efficiency (acceptance rate $= 1/(M(b-a))$ for normalized $f$)
- Change of variables / Jacobians (polar coordinates: $dA = r\,dr\,d\theta$)

## Course material

- Problem statement: [notes p. 31](../../Coursenotes/monte_carlo_2025.pdf#page=31)
- Theory: [Ch. 1 — Calculation of integrals by Monte Carlo, p. 3](../../Coursenotes/monte_carlo_2025.pdf#page=3)
- Slides: [`MCarlo-2024.pdf`](../../Coursenotes/MCarlo-2024.pdf)

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

- Histograms (normalized as densities) of each sample, overlaid with the exact $f(x)$; state $N$ and bin width.
- Hit-and-miss: measured acceptance fraction vs. theoretical value.
- Scatter plots of the disk samples (c) and (d), possibly with radial histogram showing $\propto r$.

## Implementation notes

- For (b, second item) $f$ is not given normalized: normalize numerically (e.g. `scipy.integrate.quad`) to overlay it; find $M$ from $\max f$.
- For (d): $r = \sqrt{u}$ (since $F(r) = r^2$), $\theta = 2\pi v$. A naive $r = u$ gives clustering at the center — worth showing as a contrast.

## Possible exam questions

- Why does the inverse CDF method work? What if $F$ is not invertible analytically?
- What is the efficiency of hit-and-miss and how does it depend on $M$?
- Why is $r$ uniform in $[0,1]$ wrong for a uniform disk?

## Results & notes

_To be filled in._

## AI usage log

_To be filled in (what AI helped with, for the report's AI statement)._
