"""
4.2 — Gaussian RNG (Box–Muller)

Long functions for this exercise (samplers, simulations, analysis, plotting helpers).
They are imported and run in code.ipynb, which keeps the data and figures.
"""
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
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


# =============================================================================
# Plotting
# =============================================================================

def plot_hist_xy(x, y, title=None, bins=60, mu=0.0, sigma=1.0):
    """Histograms of x and of y (area 1) with the exact N(mu, sigma^2) density on top. Returns the figure.

    mu and sigma are either one number (same for x and y) or a pair (mu_x, mu_y), (sigma_x, sigma_y).
    """
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.5), constrained_layout=True)
    mus = np.broadcast_to(np.asarray(mu, dtype=float), (2,))
    sigmas = np.broadcast_to(np.asarray(sigma, dtype=float), (2,))
    for ax, data, name, m, s in zip(axes, (x, y), ("x", "y"), mus, sigmas):
        lo, hi = m - 4 * s, m + 4 * s
        grid = np.linspace(lo, hi, 400)
        gauss = np.exp(-(grid - m)**2 / (2 * s**2)) / np.sqrt(2 * np.pi * s**2)
        ax.hist(data, bins=bins, range=(lo, hi), density=True, color=KUL_BLUES[0],
                alpha=0.6, label=f"histogram of ${name}$")
        ax.plot(grid, gauss, color="k", lw=1.5,
                label=rf"exact $\mathcal{{N}}({m:g},\,{s:g}^2)$")
        ax.set_xlabel(f"${name}$")
        ax.set_ylabel("probability density")
        ax.legend(frameon=False, fontsize=8)
    if title is not None:
        fig.suptitle(title, fontsize=9)
    return fig


def plot_xy(x, y, title=None):
    """Scatter plot of the points (x, y), with an optional info line as title. Returns the figure."""
    fig, ax = plt.subplots(figsize=(5, 5))
    if title is not None:
        ax.set_title(title, fontsize=9)
    ax.scatter(x, y, s=1, color=KUL_BLUES[0])
    ax.set_aspect("equal")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    return fig
