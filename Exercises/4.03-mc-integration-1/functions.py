"""
4.3 — Monte Carlo integration (I): importance sampling

Long functions for this exercise (samplers, simulations, analysis, plotting helpers).
They are imported and run in code.ipynb, which keeps the data and figures.
"""
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
# from numba import njit   # uncomment for hot loops (lattice / particle updates)

# --- Plot style (matches the KU Leuven report template) ------------------------
KUL_BLUES = ["#1FABD5", "#1D8DB0", "#116E8A"]
FIG_DIR = Path(__file__).resolve().parent / "figures"


def set_plot_style():
    # sans-serif everywhere (also in the math), and TrueType fonts in the pdf
    # so the report does not end up with Type 3 fonts
    plt.rcParams.update({
        "font.family": "sans-serif",
        "mathtext.fontset": "dejavusans",
        "pdf.fonttype": 42,
        "font.size": 10,
        "axes.prop_cycle": plt.cycler(color=KUL_BLUES),
        "figure.dpi": 110,
    })


def save_figure(fig, name):
    """Save a figure to figures/<name>.png and figures/<name>.pdf."""
    FIG_DIR.mkdir(exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(FIG_DIR / f"{name}.{ext}", bbox_inches="tight", dpi=200)


# --- Exercise code -------------------------------------------------------------


NORM = (2 * np.pi)**1.5   # integral of exp(-r^2/2) over R^3


def mc_estimate(n, rng):
    """One importance-sampling estimate of I from n fresh Gaussian points (x, y, z).
    
    I_N = (2 pi)^{3/2} * mean of (x + y + z)^2 over the n points.
    """
    x = norm.rvs(size=n, random_state=rng)
    y = norm.rvs(size=n, random_state=rng)
    z = norm.rvs(size=n, random_state=rng)
    return NORM * np.mean((x + y + z)**2)


def variance_vs_n(N_list, n_runs, rng):
    """For each N in N_list: n_runs independent estimates I_N, their mean and their variance.

    The variance of n_runs values is itself uncertain: for (near-)Gaussian I_N its relative
    standard error is sqrt(2 / (n_runs - 1)), used as error bar.
    Returns (mean of I_N, variance of I_N, error on that variance), one entry per N.
    """
    means, variances = [], []
    for n in N_list:
        estimates = np.array([mc_estimate(n, rng) for _ in range(n_runs)])
        means.append(estimates.mean())
        variances.append(estimates.var(ddof=1))
    variances = np.array(variances)
    return np.array(means), variances, variances * np.sqrt(2 / (n_runs - 1))


def fit_power_law(N, var, var_err):
    """Weighted straight-line fit log(var) = log(A) + b log(N).

    The error on log(var) is var_err / var, so the weights are var / var_err.
    Returns (slope b, error on b, prefactor A).
    """
    (b, log_A), cov = np.polyfit(np.log(N), np.log(var), 1, w=var / var_err, cov="unscaled")
    return b, np.sqrt(cov[0, 0]), np.exp(log_A)


def plot_variance(N, var, var_err, slope, slope_err, prefactor, var_theory, title=None):
    """Log-log plot of the variance of I_N vs N, with the power-law fit and the prediction var_theory / N.
    Returns the figure.
    """
    fig, ax = plt.subplots(figsize=(6, 3.8), constrained_layout=True)
    grid = np.logspace(np.log10(N[0]), np.log10(N[-1]), 100)
    ax.errorbar(N, var, yerr=var_err, fmt="o", ms=4, color=KUL_BLUES[1], capsize=2,
                label=r"variance of $\mathcal{I}_N$ over independent runs")
    ax.plot(grid, prefactor * grid**slope, color=KUL_BLUES[0], lw=1.5,
            label=rf"fit $\propto N^{{{slope:.3f} \pm {slope_err:.3f}}}$")
    ax.plot(grid, var_theory / grid, "k--", lw=1, label=r"prediction $18\,(2\pi)^3/N$")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("number of sampled points $N$")
    ax.set_ylabel(r"$\sigma^2(\mathcal{I}_N)$")
    ax.legend(frameon=False, fontsize=8)
    if title is not None:
        ax.set_title(title, fontsize=9)
    return fig


# =============================================================================
# (d) swapped roles: (x+y+z)^2 as density, exp(-r^2/2) as integrand
# =============================================================================

def sample_s2_density(n, L, rng):
    """n points in the box [-L, L]^3 with density p(r) proportional to s^2 = (x+y+z)^2, by rejection.

    On R^3 this density cannot be normalised, so we have to restrict it to a finite box.
    Propose uniformly in the box, accept with probability s^2 / s^2_max, where s^2_max = (3L)^2.
    """
    accepted = []
    n_have = 0
    while n_have < n:
        p = rng.uniform(-L, L, size=(2 * n, 3))
        s2 = p.sum(axis=1)**2
        keep = p[rng.random(2 * n) < s2 / (3 * L)**2]
        accepted.append(keep)
        n_have += len(keep)
    return np.concatenate(accepted)[:n]


def swapped_estimate(n, L, rng):
    """Estimate of the integral over [-L, L]^3 with p = s^2 / Z as density and g = Z exp(-r^2/2) as integrand.

    Z = int_box s^2 d^3r = (2L)^3 * L^2: the cross terms vanish and <x^2> = L^2/3 for uniform x in [-L, L].
    Z grows as L^5, so it diverges for L -> infinity: (x+y+z)^2 is not normalisable on R^3.
    Returns (estimate, standard error, relative spread per point std(g) / mean(g)).
    """
    p = sample_s2_density(n, L, rng)
    Z = (2 * L)**3 * L**2
    g = Z * np.exp(-(p**2).sum(axis=1) / 2)
    return g.mean(), g.std(ddof=1) / np.sqrt(n), g.std(ddof=1) / g.mean()


def plot_swapped(L, I_box, I_box_err, rel_spread, I_exact, rel_gauss, title=None):
    """Left: estimate of the box integral vs L, with the exact I over R^3.
    Right (log-log): relative spread per point vs L, compared with the Gaussian density.
    Returns the figure.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.8), constrained_layout=True)

    ax1.errorbar(L, I_box, yerr=I_box_err, fmt="o", ms=4, color=KUL_BLUES[1], capsize=2,
                 label=r"swapped estimate on $[-L, L]^3$")
    ax1.axhline(I_exact, color="k", lw=1, label=rf"exact $\mathcal{{I}} = {I_exact:.2f}$ on $\mathbb{{R}}^3$")
    ax1.set_xscale("log")
    ax1.set_xlabel("half-width of the box $L$")
    ax1.set_ylabel(r"$\mathcal{I}_\mathrm{box}$")
    ax1.legend(frameon=False, fontsize=8)

    ax2.plot(L, rel_spread, "o-", ms=4, color=KUL_BLUES[1],
             label=r"density $\propto (x+y+z)^2$ on $[-L, L]^3$")
    ax2.axhline(rel_gauss, color="k", ls="--", lw=1,
                label=rf"density $\propto e^{{-r^2/2}}$ on $\mathbb{{R}}^3$: {rel_gauss:.2f}")
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_xlabel("half-width of the box $L$")
    ax2.set_ylabel(r"relative spread per point $\sigma_g / \langle g \rangle$")
    ax2.legend(frameon=False, fontsize=8)

    if title is not None:
        fig.suptitle(title, fontsize=9)
    return fig
