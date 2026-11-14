# 4.1 — Non-uniform random numbers

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| ✅ yes | simulation (+ short proof) | [p. 31–32](../../Coursenotes/monte_carlo_2025.pdf#page=31) | ⬜ todo |

## Question

Generate random numbers with a given probability density $f(x)$ ($f\ge 0$, $\int f = 1$)
from uniform random numbers in $[0,1]$, using two methods:

- **Inverse CDF:** with $F(x) = \int_{-\infty}^{x} f(y)\,dy$, if $x_i \sim U[0,1]$ then
  $y_i = F^{-1}(x_i)$ is distributed with density $f$ (show this — "easy and left to you").
  Requires $F$ to be analytic and invertible.
- **Hit-and-miss:** for $f$ supported on $[a,b]$ with $M > f(x)$, draw $t\sim U[a,b]$,
  $s\sim U[0,M]$; keep $t$ if $s \le f(t)$ (hit), discard otherwise (miss).

**Sub-questions**

- [ ] (0) Prove that $y = F^{-1}(x)$ with $x\sim U[0,1]$ has density $f$.
- [ ] (a) Inverse CDF — generate and histogram numbers distributed
  - [ ] uniformly in $[-2, 1]$
  - [ ] exponentially on $\mathbb{R}^+$: $f(x) = e^{-x}$ for $x\ge 0$
  - [ ] linearly on $[-1,1]$: $f(x) = (x+1)/2$
- [ ] (b) Hit-and-miss — generate and histogram numbers distributed
  - [ ] linearly on $[-1,1]$: $f(x) = (x+1)/2$
  - [ ] $f(x) = -x(1-x)\,e^{-x^2}\log(1-x)$ on $[0,1]$
- [ ] (c) Hit-and-miss: points uniformly distributed inside a circle of radius $R=1$.
- [ ] (d) Same uniform disk *without* hit-and-miss, using an appropriate density $f(r,\theta)$ in polar coordinates.

## Relevant topics

- Inverse transform sampling, cumulative distribution function — [Ch. 1, p. 3](../../Coursenotes/monte_carlo_2025.pdf#page=3)
- Rejection (hit-and-miss) sampling and its efficiency (acceptance rate $= 1/(M(b-a))$ for normalized $f$)
- Change of variables / Jacobians (polar coordinates: $dA = r\,dr\,d\theta$)

## Course material

- Problem statement: [notes p. 31](../../Coursenotes/monte_carlo_2025.pdf#page=31)
- Theory: [Ch. 1 — Calculation of integrals by Monte Carlo, p. 3](../../Coursenotes/monte_carlo_2025.pdf#page=3)
- Slides: [`MCarlo-2024.pdf`](../../Coursenotes/MCarlo-2024.pdf)

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
