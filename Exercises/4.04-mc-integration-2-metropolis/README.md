# 4.4 — Monte Carlo integration (II): Metropolis

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| ✅ yes | simulation | [p. 34–35](../../Coursenotes/monte_carlo_2025.pdf#page=34) | 🟨 code done, report todo |

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

- [x] (a) Plot the $(x, y)$ trajectory for $N = 10^4$ steps starting at $\mathbf r = (0,0,0)$ and at $\mathbf r = (10,10,10)$, for $h = 1$ and $h = 0.1$. With a run of $N = 10^6$ points, verify via histograms that the equilibrium distribution is $\propto e^{-r^2/2}$.
- [x] (b) Estimate the integral with Metropolis and compare with [4.3](../4.03-mc-integration-1/).
- [x] (c) Estimate the equilibration time $N_{eq}$ starting from $(10,10,10)$ for $h = 1$ and $h = 0.1$.
- [x] (d) Which algorithm do you expect to be better for this calculation: direct Gaussian sampling or Metropolis? Why?

## Relevant topics

- Markov chains, detailed balance, Metropolis algorithm — [§2.1, p. 7](../../Coursenotes/monte_carlo_2025.pdf#page=7), [§2.3, p. 9](../../Coursenotes/monte_carlo_2025.pdf#page=9), [§2.4, p. 10](../../Coursenotes/monte_carlo_2025.pdf#page=10)
- Equilibration — [§2.5, p. 11](../../Coursenotes/monte_carlo_2025.pdf#page=11)
- Correlation time and effective number of independent samples — [§2.6, p. 12](../../Coursenotes/monte_carlo_2025.pdf#page=12)
- Choice of step size $h$ (acceptance rate vs. step length)

## Course material

- Problem statement: [notes p. 34](../../Coursenotes/monte_carlo_2025.pdf#page=34)
- Theory: [Ch. 2, p. 6–16](../../Coursenotes/monte_carlo_2025.pdf#page=6)

## Files

| File | Content |
|---|---|
| [`functions.py`](functions.py) | Plotting helpers only (`save_figure`, `KUL_BLUES`, one `plot_*` per figure). |
| [`code.ipynb`](code.ipynb) | Parameters, the Metropolis sampler (`metropolis`), the blocking error (`blocking_error`), data, figures and numbers, one section per sub-question. |
| [`figures/`](figures/) | Saved plots (`.png` + `.pdf`) used in the report. |

The module is called `functions.py` and not `code.py`, because a `code.py` would hide
Python's built-in `code` module, which IPython/Jupyter need. Thanks to
`%autoreload 2`, edits to `functions.py` are picked up by the notebook without a kernel restart.

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

All runs: `SEED = 1` (`np.random.default_rng`), one generator used in order through the notebook.
The sampler `metropolis(r0, h, n_steps, rng)` is written out in the notebook. It runs several chains side
by side (one row per chain), so one function covers the single runs and the 100-chain average of (c).

### (a) Trajectories and equilibrium distribution

- [`trajectories`](figures/trajectories.png): $10^4$ steps for each start point and $h$.
  - $h = 1$ (acceptance 0.81): from the origin the chain fills the Gaussian blob $|x|, |y| \lesssim 3$; from
    $(10,10,10)$ it walks straight to the origin in a few hundred steps and then stays there.
  - $h = 0.1$ (acceptance 0.94–0.99): a slow random walk. From the origin it covers only a part of the blob in $10^4$ steps;
    from $(10,10,10)$ it only just reaches the origin region at the end.
- [`histograms`](figures/histograms.png): $10^6$ steps from the origin, after discarding $2\times10^4$ steps.
  The $x, y, z$ histograms follow $e^{-x^2/2}/\sqrt{2\pi}$ and the $r$ histogram follows $\sqrt{2/\pi}\,r^2e^{-r^2/2}$.
  - $h = 1$: $\langle x^2\rangle, \langle y^2\rangle, \langle z^2\rangle = 1.002, 1.000, 1.001$ (exact 1).
  - $h = 0.1$: $1.023, 0.964, 1.025$, and the histograms are visibly noisier. Same number of points, but far fewer independent ones.

### (b) Integral

$I = (2\pi)^{3/2}\langle (x+y+z)^2\rangle$ averaged over the chain; error from blocking with $B = 8192$
([`blocking`](figures/blocking.png)). The blocked error rises with $B$ and levels off once $B \gg \tau$.

| method | $N$ | $I$ | naive error | $\tau_\text{int}$ (steps) |
|---|---|---|---|---|
| exact | – | 47.249 | – | – |
| Gaussian, 4.3 (b) | $10^6$ | $47.241 \pm 0.067$ | 0.067 | 1/2 |
| Metropolis, $h = 1$ | $10^6$ | $47.64 \pm 0.42$ | 0.067 | $19 \pm 2$ |
| Metropolis, $h = 0.1$ | $10^6$ | $43.5 \pm 2.3$ | 0.059 | $770 \pm 100$ |

- Both Metropolis results agree with the exact value (+0.9 and −1.6 error bars).
- For the same $N$ the error is $\sqrt{2\tau_\text{int}}$ times the Gaussian one: 6× larger for $h = 1$, 40× for $h = 0.1$.
- For $h = 0.1$ the blocking curve has not fully levelled off at $B = 8192$ (there are only ~$N/2\tau \approx 600$
  independent points), so this error bar is a slight underestimate.
- The naive $s_f/\sqrt N$ is about the same as in 4.3, but it is wrong here because it ignores the correlations.

### (c) Equilibration time from $(10,10,10)$

100 independent chains of $2\times10^4$ steps; $N_{eq}$ = first step at which the chain average of $r^2$ drops below
$3 + 2\sqrt{6/100} = 3.49$ ($r^2 \sim \chi^2_3$ in equilibrium, variance 6) ([`equilibration`](figures/equilibration.png)).

| $h$ | $N_{eq}$ | small-$h$ estimate $\frac{12}{h^2}\ln\frac{297}{0.49}$ |
|---|---|---|
| 1 | 205 | 77 |
| 0.1 | 8485 | 7689 |

- Small-$h$ estimate: one Metropolis step has mean displacement $\frac{\sigma^2}{2}\nabla\ln w = -\frac{h^2}{24}\mathbf r$
  ($\sigma^2 = h^2/12$ per component), so $\langle r^2\rangle - 3 \approx 297\,e^{-h^2t/12}$ and $N_{eq} \propto 1/h^2$.
- It works for $h = 0.1$. For $h = 1$ it is too optimistic: far from the origin $r'^2 - r^2 \approx 2\mathbf r\cdot\boldsymbol\delta$
  is large, so nearly every outward step is rejected, and the walk moves inward at a roughly constant speed instead of exponentially
  ($r$ goes from 17.3 to about 3 in ~150 steps, ≈ 0.1 per step).
- The $N_{eq} = 2\times10^4$ steps discarded in (a), (b), (d) are well above both values.

### (d) Gaussian sampling or Metropolis?

Scan of $h$, $5\times10^5$ steps each, $\tau_\text{int}$ from blocking ($B = 8192$) ([`h_scan`](figures/h_scan.png)):

| $h$ | 0.1 | 0.2 | 0.5 | 1 | 2 | 3 | 5 | 10 | 20 |
|---|---|---|---|---|---|---|---|---|---|
| acceptance | 0.98 | 0.96 | 0.90 | 0.81 | 0.63 | 0.48 | 0.26 | 0.053 | 0.006 |
| $\tau_\text{int}$ | 1041 | 317 | 69 | 18.5 | 5.5 | 5.1 | 4.6 | 15 | 147 |

- Small $h$: almost everything is accepted, but the steps are tiny (diffusion, $\tau \propto 1/h^2$).
  Large $h$: the proposals land far out in the tails and are rejected, so the chain stands still.
  The best value is in between, $h \approx 2$–$5$ (acceptance 0.25–0.6), with $\tau_\text{int} \approx 5$.
- Even then, a chain of $N$ steps is worth only $N/(2\tau_\text{int}) \approx N/10$ independent points.
  A Metropolis step costs about as much as drawing 3 Gaussian numbers, so direct Gaussian sampling is at least
  10× cheaper for the same error. It also needs no equilibration and no blocking analysis.
- Metropolis is worth it when $w$ cannot be sampled directly (many coupled variables, e.g. the Ising model), or when the
  normalisation of $w$ is unknown: only the ratio $w(\mathbf r')/w(\mathbf r)$ enters the acceptance.

### Answers to the exam questions

- *Why does detailed balance + ergodicity give $w$?* Detailed balance makes $w$ a stationary distribution of the chain;
  ergodicity (every point reachable, here with uniform steps of any $h > 0$) makes it the unique one,
  and the chain converges to it from any start.
- *Why is $h = 0.1$ slow, and what if $h$ is very large?* See (d): diffusion with tiny steps vs. almost all moves rejected.
- *Why are the Metropolis error bars larger than $\sigma/\sqrt N$?* Successive points are correlated; the effective number
  of independent points is $N/(2\tau_\text{int})$, so the error is $\sqrt{2\tau_\text{int}}\,s_f/\sqrt N$.
