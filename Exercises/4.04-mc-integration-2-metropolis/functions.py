"""
4.4 — Monte Carlo integration (II): Metropolis

Plotting helpers only. The Metropolis algorithm and the analysis (blocking, equilibration)
are written out in code.ipynb, so the important code is all in one place.
"""
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

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


def plot_trajectories(runs, title=None):
    """2x2 grid of (x, y) trajectories. runs is a dict {(start label, h): chain of shape (N, 3)}."""
    fig, axes = plt.subplots(2, 2, figsize=(8, 7), constrained_layout=True)
    for ax, ((start, h), chain) in zip(axes.flat, runs.items()):
        ax.plot(chain[:, 0], chain[:, 1], lw=0.4, color=KUL_BLUES[1])
        ax.plot(chain[0, 0], chain[0, 1], "o", ms=5, color="k", label="start")
        ax.plot(chain[-1, 0], chain[-1, 1], "s", ms=5, color=KUL_BLUES[0], label="end")
        ax.set_title(f"start {start}, $h = {h}$", fontsize=9)
        ax.set_xlabel("$x$")
        ax.set_ylabel("$y$")
        ax.set_aspect("equal", adjustable="datalim")
        ax.legend(frameon=False, fontsize=8)
    if title is not None:
        fig.suptitle(title, fontsize=9)
    return fig


def plot_histograms(samples, title=None):
    """Histograms of x, y, z and r = |r| for each h, against the exact densities.

    samples is a dict {h: chain of shape (N, 3)}.
    Exact: x, y, z ~ N(0, 1), and r has density sqrt(2/pi) r^2 exp(-r^2/2) (Maxwell).
    """
    fig, axes = plt.subplots(1, 4, figsize=(12, 3.2), constrained_layout=True)
    grid_x = np.linspace(-4.5, 4.5, 200)
    grid_r = np.linspace(0, 5, 200)
    exact_x = np.exp(-grid_x**2 / 2) / np.sqrt(2 * np.pi)
    exact_r = np.sqrt(2 / np.pi) * grid_r**2 * np.exp(-grid_r**2 / 2)
    for i, (h, chain) in enumerate(samples.items()):
        style = dict(bins=60, density=True, histtype="step", lw=1.3, color=KUL_BLUES[2 * i], label=f"$h = {h}$")
        for k, name in enumerate("xyz"):
            axes[k].hist(chain[:, k], range=(-4.5, 4.5), **style)
        axes[3].hist(np.linalg.norm(chain, axis=1), range=(0, 5), **style)
    for k, name in enumerate("xyz"):
        axes[k].plot(grid_x, exact_x, "k--", lw=1, label=r"$e^{-%s^2/2}/\sqrt{2\pi}$" % name)
        axes[k].set_xlabel(f"${name}$")
    axes[3].plot(grid_r, exact_r, "k--", lw=1, label=r"$\sqrt{2/\pi}\,r^2 e^{-r^2/2}$")
    axes[3].set_xlabel("$r$")
    axes[0].set_ylabel("probability density")
    for ax in axes:
        ax.legend(frameon=False, fontsize=7)
    if title is not None:
        fig.suptitle(title, fontsize=9)
    return fig


def plot_blocking(block_sizes, errors, naive, title=None):
    """Error of the mean vs block size B (log-log). errors / naive are dicts {h: values / value}.
    The naive error (B = 1, treats the points as independent) is drawn as a dashed line."""
    fig, ax = plt.subplots(figsize=(6, 3.8), constrained_layout=True)
    for i, h in enumerate(errors):
        ax.plot(block_sizes, errors[h], "o-", ms=4, color=KUL_BLUES[2 * i], label=f"$h = {h}$, blocked")
        ax.axhline(naive[h], color=KUL_BLUES[2 * i], ls="--", lw=1, label=rf"$h = {h}$, naive $s_f/\sqrt{{N}}$")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("block size $B$ (Metropolis steps)")
    ax.set_ylabel(r"standard error of $\mathcal{I}_\mathrm{MC}$")
    ax.legend(frameon=False, fontsize=8)
    if title is not None:
        ax.set_title(title, fontsize=9)
    return fig


def plot_equilibration(r2_mean, r2_single, n_eq, r2_eq=3.0, title=None):
    """r^2 vs Metropolis step, one panel per h: a single chain and the average over many chains.
    r2_mean, r2_single and n_eq are dicts {h: ...}; r2_eq is the equilibrium value <r^2> = 3."""
    fig, axes = plt.subplots(1, len(r2_mean), figsize=(10, 3.8), constrained_layout=True)
    for ax, h in zip(axes, r2_mean):
        t = np.arange(1, len(r2_mean[h]) + 1)
        ax.plot(t, r2_single[h], lw=0.5, color=KUL_BLUES[0], label="one chain")
        ax.plot(t, r2_mean[h], lw=1.5, color=KUL_BLUES[2], label="average over chains")
        ax.axhline(r2_eq, color="k", lw=1, label=r"equilibrium $\langle r^2 \rangle = 3$")
        ax.axvline(n_eq[h], color="k", ls="--", lw=1, label=f"$N_{{eq}} = {n_eq[h]}$")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlabel("Metropolis step $t$")
        ax.set_ylabel("$r^2(t)$")
        ax.set_title(f"$h = {h}$", fontsize=9)
        ax.legend(frameon=False, fontsize=8)
    if title is not None:
        fig.suptitle(title, fontsize=9)
    return fig


def plot_h_scan(h, acceptance, tau, title=None):
    """Acceptance rate and integrated autocorrelation time of f = (x+y+z)^2 vs step size h."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.6), constrained_layout=True)
    ax1.plot(h, acceptance, "o-", ms=4, color=KUL_BLUES[1])
    ax1.set_xscale("log")
    ax1.set_xlabel("step size $h$")
    ax1.set_ylabel("acceptance rate")
    ax2.plot(h, tau, "o-", ms=4, color=KUL_BLUES[1], label="Metropolis")
    ax2.axhline(0.5, color="k", ls="--", lw=1, label=r"independent Gaussian points: $\tau_\mathrm{int} = 1/2$")
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_xlabel("step size $h$")
    ax2.set_ylabel(r"$\tau_\mathrm{int}$ of $(x+y+z)^2$ (steps)")
    ax2.legend(frameon=False, fontsize=8)
    if title is not None:
        fig.suptitle(title, fontsize=9)
    return fig
