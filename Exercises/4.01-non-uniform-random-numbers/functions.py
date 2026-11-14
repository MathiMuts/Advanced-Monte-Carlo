"""
4.1 — Non-uniform random numbers

Long functions for this exercise (samplers, simulations, analysis, plotting helpers).
They are imported and run in code.ipynb, which keeps the data and figures.
"""
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

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


# =============================================================================
# (a) Inverse CDF method
#     Draw u ~ U[0,1] and return x = F^{-1}(u).
# =============================================================================

# =============================================================================
# (b) Hit-and-miss method
# =============================================================================

# =============================================================================
# (c) and (d) Uniform points in the unit disk
# =============================================================================

# =============================================================================
# Analysis and plotting
# =============================================================================

def plot_histogram(ax, samples, f, lo, hi, bins, title):
    """Histogram of the samples (scaled so its area is 1) with the exact density f on top."""
    counts, edges = np.histogram(samples, bins=bins, range=(lo, hi))
    width = edges[1] - edges[0]
    centres = (edges[:-1] + edges[1:]) / 2
    n = len(samples)

    # divide by n * width, so the bars have total area 1 and can be compared with f
    height = counts / (n * width)
    # a bin with k numbers in it fluctuates by about sqrt(k) from run to run
    error = np.sqrt(counts) / (n * width)

    ax.bar(centres, height, width=width, color=KUL_BLUES[0], alpha=0.5,
           label=f"histogram, {n:,} numbers")
    ax.errorbar(centres, height, yerr=error, fmt="none", ecolor=KUL_BLUES[2], elinewidth=0.8)

    x = np.linspace(lo, hi, 1001)[1:-1]   # skip the end points (log(0) in one of the f's)
    ax.plot(x, f(x), color="k", lw=1.5, label="exact density")

    ax.set_xlabel("$x$")
    ax.set_ylabel("probability density")
    ax.set_title(title)
    ax.legend(frameon=False, fontsize=8)
