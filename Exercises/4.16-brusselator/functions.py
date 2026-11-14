"""
4.16 — Brusselator

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


def save_figure(fig, name):
    """Save a figure to figures/<name>.png and figures/<name>.pdf."""
    FIG_DIR.mkdir(exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(FIG_DIR / f"{name}.{ext}", bbox_inches="tight", dpi=200)


# --- Exercise code -------------------------------------------------------------
