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

def sample_uniform(a, b, n, rng):
    # f(x) = 1/(b-a) on [a,b]  ->  F(x) = (x-a)/(b-a)  ->  x = a + (b-a) u
    u = rng.random(n)
    return a + (b - a) * u


def sample_exponential(n, rng):
    # f(x) = e^{-x} for x >= 0  ->  F(x) = 1 - e^{-x}  ->  x = -log(1-u)
    # (rng.random gives u in [0,1), so 1-u is never 0 and the log is safe)
    u = rng.random(n)
    return -np.log(1 - u)


def sample_linear_inverse(n, rng):
    # f(x) = (x+1)/2 on [-1,1]  ->  F(x) = (x+1)^2/4  ->  x = 2 sqrt(u) - 1
    u = rng.random(n)
    return 2 * np.sqrt(u) - 1


# The densities themselves, to draw on top of the histograms
def uniform_pdf(x, a, b):
    return np.where((x >= a) & (x <= b), 1 / (b - a), 0.0)


def exponential_pdf(x):
    return np.where(x >= 0, np.exp(-x), 0.0)


def linear_pdf(x):
    return np.where(np.abs(x) <= 1, (x + 1) / 2, 0.0)


# =============================================================================
# (b) Hit-and-miss method
# =============================================================================

def weird_function(x):
    # f(x) = -x (1-x) e^{-x^2} log(1-x) on [0,1]   (NOT normalized)
    # At x = 1 the product (1-x) log(1-x) -> 0, so we set f(1) = 0 by hand.
    x = np.asarray(x, dtype=float)
    result = np.zeros_like(x)
    inside = (x >= 0) & (x < 1)
    xi = x[inside]
    result[inside] = -xi * (1 - xi) * np.exp(-xi**2) * np.log(1 - xi)
    return result


def normalization(f, a, b):
    # Z = integral of f over [a,b], so that f/Z is a proper density
    Z, _ = quad(lambda x: float(f(np.array([x]))[0]), a, b)
    return Z


def find_bound(f, a, b, safety=1.05):
    # The method needs M > f(x) everywhere on [a,b].
    # Take the maximum on a fine grid and add 5% to be on the safe side.
    x = np.linspace(a, b, 100_001)
    return safety * np.max(f(x))


def hit_and_miss(f, a, b, M, n, rng):
    """Generate n numbers distributed as f on [a,b] (f does not need to be normalized).

    Draw t ~ U[a,b] and s ~ U[0,M]. If s <= f(t) it is a hit and t is kept,
    otherwise it is a miss and the pair is thrown away.
    Returns the accepted numbers and the fraction of hits.
    """
    accepted = []
    n_accepted = 0
    n_tried = 0

    # Work in batches instead of one number at a time (much faster in numpy).
    while n_accepted < n:
        batch = 2 * (n - n_accepted) + 1000
        t = rng.uniform(a, b, batch)
        s = rng.uniform(0, M, batch)
        hit = s <= f(t)

        # Only keep as many hits as we still need, and count the tries up to
        # the last hit we keep (otherwise the acceptance fraction is slightly off).
        need = n - n_accepted
        positions = np.flatnonzero(hit)[:need]
        accepted.append(t[positions])
        n_accepted += len(positions)
        n_tried += batch if len(positions) < need else positions[-1] + 1

    return np.concatenate(accepted), n / n_tried


# =============================================================================
# (c) and (d) Uniform points in the unit disk
# =============================================================================

def disk_hit_and_miss(n, rng):
    # Throw points uniformly in the square [-1,1]^2 and keep the ones inside the circle.
    # Expected acceptance = area circle / area square = pi/4.
    xs, ys = [], []
    n_accepted = 0
    n_tried = 0
    while n_accepted < n:
        batch = 2 * (n - n_accepted) + 1000
        x = rng.uniform(-1, 1, batch)
        y = rng.uniform(-1, 1, batch)
        inside = x**2 + y**2 <= 1

        # only keep as many as we still need, and count the tries up to that point
        need = n - n_accepted
        positions = np.flatnonzero(inside)[:need]
        xs.append(x[positions])
        ys.append(y[positions])
        n_accepted += len(positions)
        n_tried += batch if len(positions) < need else positions[-1] + 1
    return np.concatenate(xs), np.concatenate(ys), n / n_tried


def disk_polar(n, rng):
    # Uniform in the disk: f(r, theta) dr dtheta = (1/pi) r dr dtheta
    #   = [2r dr] * [dtheta / (2 pi)]   -> r and theta are independent.
    # theta ~ U[0, 2pi]; r has F(r) = r^2, so r = sqrt(u).
    r = np.sqrt(rng.random(n))
    theta = 2 * np.pi * rng.random(n)
    return r * np.cos(theta), r * np.sin(theta)


def disk_polar_naive(n, rng):
    # WRONG on purpose: r uniform in [0,1] forgets the Jacobian r of dA = r dr dtheta,
    # so too many points end up near the centre.
    r = rng.random(n)
    theta = 2 * np.pi * rng.random(n)
    return r * np.cos(theta), r * np.sin(theta)


# =============================================================================
# Analysis and plotting
# =============================================================================

def density_histogram(samples, bins, value_range):
    """Histogram normalized as a probability density, with error bars.

    We divide by the TOTAL number of samples (also the ones outside the plotted range),
    so the bars can be compared directly with f(x).
    The count in a bin is ~ binomial, error ~ sqrt(count) for many bins.
    """
    counts, edges = np.histogram(samples, bins=bins, range=value_range)
    width = edges[1] - edges[0]
    n = len(samples)
    centres = (edges[:-1] + edges[1:]) / 2
    density = counts / (n * width)
    error = np.sqrt(counts) / (n * width)
    return centres, density, error, width


def plot_density(ax, samples, pdf, value_range, bins=50, title=""):
    centres, density, error, width = density_histogram(samples, bins, value_range)
    ax.bar(centres, density, width=width, color=KUL_BLUES[0], alpha=0.5,
           label=f"histogram, N = {len(samples):,}")
    ax.errorbar(centres, density, yerr=error, fmt="none", ecolor=KUL_BLUES[2],
                elinewidth=0.8, capsize=0)

    x = np.linspace(*value_range, 500)
    ax.plot(x, pdf(x), color="k", lw=1.5, label="exact $f(x)$")
    ax.set_xlabel("$x$")
    ax.set_ylabel("probability density")
    ax.set_title(title)
    ax.legend(frameon=False, fontsize=8)


def mean_with_error(samples):
    # sample mean and its standard error sigma/sqrt(N) (samples are independent)
    return np.mean(samples), np.std(samples, ddof=1) / np.sqrt(len(samples))


def exact_mean(pdf, a, b):
    m, _ = quad(lambda x: x * float(pdf(np.array([x]))[0]), a, b)
    return m


def plot_disk(ax, x, y, title, n_show=5000):
    # Only draw part of the points, otherwise the scatter plot is just a blue blob.
    ax.scatter(x[:n_show], y[:n_show], s=1, color=KUL_BLUES[1])
    circle = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(circle), np.sin(circle), color="k", lw=1)
    ax.set_aspect("equal")
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_title(title)
