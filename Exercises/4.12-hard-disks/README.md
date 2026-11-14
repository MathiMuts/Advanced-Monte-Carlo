# 4.12 — Hard disks

| Required | Type | Problem in notes | Status |
|---|---|---|---|
| ✅ yes | analytical + simulation | [p. 44–46](../../Coursenotes/monte_carlo_2025.pdf#page=44) | ⬜ todo |

## Question

Hard disks of radius $\sigma$ in 2D: $V_{HS}(r) = +\infty$ if $r < 2\sigma$, $0$ otherwise.
Metropolis: pick a particle $i$, move $\mathbf r_i' = \mathbf r_i + \boldsymbol\delta$,
accept if $|\mathbf r_j - \mathbf r_i'| \ge 2\sigma$ for all $j\neq i$, otherwise reject.
Shift $\delta_\alpha = (2u-1)\,q$ ($u\sim U[0,1]$, $q$ a characteristic length, typically
$q\approx L/\sqrt N$). $L\times L$ box with periodic boundaries:
$\mathbf r_i' = \mathbf r_i + \boldsymbol\delta - L\,\mathrm{floor}\!\left(\frac{\mathbf r_i+\boldsymbol\delta}{L}\right)$
(same for distances — minimum image). Optional speed-up: **cell lists** with cells of
size $r_c \gtrsim 2\sigma$.

Radial distribution function:

$$g(r) = \frac{L^2}{2\pi r N^2}\Big\langle\sum_i\sum_{j\neq i}\delta(r - r_{ij})\Big\rangle \approx \frac{\Delta N(r,\Delta r)}{2\pi r\,\Delta r\,\rho},$$

with $\Delta N$ the average number of neighbours at distance $[r, r+\Delta r]$ and $\rho = N/L^2$.
For hard disks $g(r) = 0$ for $r < 2\sigma$; $g\approx 1$ beyond for a dilute gas.

**Sub-questions**

- [ ] (a) Packing fraction $\eta = N\pi R^2/L^2$: what is its maximal possible value? (analytical)
- [ ] (b) $L = 100$, $R = 2$: compute the average acceptance ratio for several $\eta$ and some given $q$.
- [ ] (c) Compute $g(r)$ for several $\eta$; show that $g(r)$ becomes oscillatory at high $\eta$.
- [ ] (d) *Optional:* implement cell lists and compare with the standard algorithm.

## Relevant topics

- Continuous systems, Lennard-Jones fluids, $g(r)$ — [§2.12, p. 25](../../Coursenotes/monte_carlo_2025.pdf#page=25)
- Metropolis with infinite-energy rejection — [§2.4, p. 10](../../Coursenotes/monte_carlo_2025.pdf#page=10)
- Periodic boundaries / minimum image convention, cell lists (Fig. 15)
- Close packing (hexagonal lattice), liquid structure

## Course material

- Problem statement: [notes p. 44](../../Coursenotes/monte_carlo_2025.pdf#page=44), Fig. 15 on [p. 46](../../Coursenotes/monte_carlo_2025.pdf#page=46)
- Footnote 25 (p. 46): average $g(r)$ over many equilibrated configurations; **validate the $g(r)$ code on an ideal gas** (random points must give $g=1$).

## Deliverables for the report

- Derivation of $\eta_\text{max}$ (hexagonal packing).
- Acceptance ratio vs. $\eta$ (and vs. $q$).
- $g(r)$ curves for several $\eta$ (incl. ideal-gas test), with $N$, number of sweeps and number of configurations averaged.
- Snapshot of a configuration at high $\eta$.
- (Optional) CPU time per sweep vs. $N$, naive $O(N)$ vs. cell list $O(1)$ per move.

## Implementation notes

- Initialize on a (hexagonal or square) lattice for high $\eta$; random insertion fails at high density.
- Only compute $g(r)$ up to $r_\text{max} \le L/2$.
- Use `numba` for the overlap check.

## Possible exam questions

- Why is there no temperature in the hard-disk problem? (Entropy-driven ordering)
- What do the peaks of $g(r)$ mean physically?
- How does the cell list change the computational complexity?

## Results & notes

_To be filled in._

## AI usage log

_To be filled in._
