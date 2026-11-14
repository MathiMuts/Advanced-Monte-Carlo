# 4.4 — Monte Carlo integration (II): Metropolis

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| ✅ yes | simulation | [p. 34–35](../../Coursenotes/monte_carlo_2025.pdf#page=34) | ⬜ todo |

## Question

Recompute the integral of [4.3](../4.03-mc-integration-1/) with the Metropolis algorithm:
a Markov chain whose stationary distribution is
$w(\mathbf r) = (2\pi)^{-3/2}\exp(-r^2/2)$. Detailed balance requires

$$\frac{P(\mathbf r\to\mathbf r')}{P(\mathbf r'\to\mathbf r)} = \frac{w(\mathbf r')}{w(\mathbf r)} = \exp\!\left(-\frac{r'^2-r^2}{2}\right).$$

Split $P = g\,A$. Selection $g$: $\mathbf r' = \mathbf r + \boldsymbol\delta$ with each component
of $\boldsymbol\delta$ independently from $W_h(\delta) = 1/h$ for $|\delta| < h/2$ (0 otherwise).
Acceptance:

$$A = \begin{cases} 1 & r'^2 - r^2 < 0 \\ \exp\!\left(-\frac{r'^2-r^2}{2}\right) & \text{otherwise.}\end{cases}$$

**Sub-questions**

- [ ] (a) Plot the $(x, y)$ trajectory for $N = 10^4$ steps starting at $\mathbf r = (0,0,0)$ and at $\mathbf r = (10,10,10)$, for $h = 1$ and $h = 0.1$. With a run of $N = 10^6$ points, verify via histograms that the equilibrium distribution is $\propto e^{-r^2/2}$.
- [ ] (b) Estimate the integral with Metropolis and compare with [4.3](../4.03-mc-integration-1/).
- [ ] (c) Estimate the equilibration time $N_{eq}$ starting from $(10,10,10)$ for $h = 1$ and $h = 0.1$.
- [ ] (d) Which algorithm do you expect to be better for this calculation: direct Gaussian sampling or Metropolis? Why?

## Relevant topics

- Markov chains, detailed balance, Metropolis algorithm — [§2.1, p. 7](../../Coursenotes/monte_carlo_2025.pdf#page=7), [§2.3, p. 9](../../Coursenotes/monte_carlo_2025.pdf#page=9), [§2.4, p. 10](../../Coursenotes/monte_carlo_2025.pdf#page=10)
- Equilibration — [§2.5, p. 11](../../Coursenotes/monte_carlo_2025.pdf#page=11)
- Correlation time and effective number of independent samples — [§2.6, p. 12](../../Coursenotes/monte_carlo_2025.pdf#page=12)
- Choice of step size $h$ (acceptance rate vs. step length)

## Course material

- Problem statement: [notes p. 34](../../Coursenotes/monte_carlo_2025.pdf#page=34)
- Theory: [Ch. 2, p. 6–16](../../Coursenotes/monte_carlo_2025.pdf#page=6)

## Deliverables for the report

- Trajectory plots (4 combinations of start point × $h$).
- Histograms of $x$, $y$, $z$ (or $r$) from the $10^6$-step run vs. the exact marginal densities.
- Integral estimate with a *correlated-data* error bar (blocking or autocorrelation time), compared to 4.3.
- $r^2(t)$ or $x(t)$ vs. step showing equilibration; $N_{eq}$ for both $h$; acceptance rates.

## Implementation notes

- Rejected moves still count: the old point is re-added to the sample.
- Discard the first $N_{eq}$ steps before averaging.

## Possible exam questions

- Why does detailed balance + ergodicity guarantee convergence to $w$?
- Why is $h=0.1$ slow and what happens if $h$ is very large?
- Why are the Metropolis error bars larger than naive $\sigma/\sqrt N$?

## Results & notes

_To be filled in._

## AI usage log

_To be filled in._
