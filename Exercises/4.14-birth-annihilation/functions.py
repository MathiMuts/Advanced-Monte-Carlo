"""
4.14 — Birth–annihilation process

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
