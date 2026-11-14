# Advanced Monte Carlo Simulations — Exercises

Solutions, simulation code and report material for the exercises of the course
**Advanced Monte Carlo Simulations** (Prof. Enrico Carlon, KU Leuven, academic year 2026–2027).

The course covers Monte Carlo integration, Markov-chain Monte Carlo for systems in
equilibrium (Metropolis, Wolff, heat bath, Kawasaki, umbrella sampling, parallel
tempering, continuous-time MC, hard disks / Lennard-Jones fluids) and stochastic
simulation of out-of-equilibrium systems (Gillespie algorithm for coupled chemical
reactions).

## Course material

| File | Content |
|---|---|
| [`Coursenotes/monte_carlo_2025.pdf`](Coursenotes/monte_carlo_2025.pdf) | Lecture notes (51 p.). Theory in Ch. 1–3, problems in Ch. 4 (p. 31–48), Ising/Potts and master equation in the appendices. |
| [`Coursenotes/MCarlo-2024.pdf`](Coursenotes/MCarlo-2024.pdf) | Handwritten lecture slides (2024). |
| [`Coursenotes/exam.txt`](Coursenotes/exam.txt) | Assignment and exam instructions. |

### Lecture notes overview

| Chapter | Topic | Page |
|---|---|---|
| 1 | Calculation of integrals by Monte Carlo | [3](Coursenotes/monte_carlo_2025.pdf#page=3) |
| 2.1–2.3 | Markov chains, ergodicity, detailed balance | [7](Coursenotes/monte_carlo_2025.pdf#page=7) |
| 2.4–2.7 | Metropolis, equilibration, correlation time, critical slowing down | [10](Coursenotes/monte_carlo_2025.pdf#page=10) |
| 2.8 | Wolff cluster algorithm | [17](Coursenotes/monte_carlo_2025.pdf#page=17) |
| 2.9 | Heat bath algorithm | [19](Coursenotes/monte_carlo_2025.pdf#page=19) |
| 2.10 | Conserved order parameter Ising model (Kawasaki) | [21](Coursenotes/monte_carlo_2025.pdf#page=21) |
| 2.11 | Umbrella sampling, parallel tempering, continuous-time MC | [22](Coursenotes/monte_carlo_2025.pdf#page=22) |
| 2.12 | Continuous systems: Lennard-Jones fluids | [25](Coursenotes/monte_carlo_2025.pdf#page=25) |
| 3 | Out of equilibrium: rate equations, Gillespie algorithm | [27](Coursenotes/monte_carlo_2025.pdf#page=27) |
| 4 | **Problems** | [31](Coursenotes/monte_carlo_2025.pdf#page=31) |
| A, B | Ising & Potts models, master equation | [49](Coursenotes/monte_carlo_2025.pdf#page=49) |

## Assignment

- Solve problems **4.1–4.8** and **4.12–4.16**, plus **at least one of 4.9, 4.10, 4.11**.
- Write a report (max. 25 pages, single PDF) with the solutions and simulation results:
  every graph needs labelled axes, clearly identified quantities and the simulation
  details (parameters, number of samples, ...). End the report with a statement on how AI was used.
- Upload the report and the code to the two Toledo assignments at least one day before the exam.
- Exam: written closed-book theory questions, followed by a 15–20 min oral discussion of
  the written answers, the report and the code (bringing a laptop to run the code is optional).

## Exercises

| # | Exercise | Required | Topics | Status |
|---|---|---|---|---|
| 4.1 | [Non-uniform random numbers](Exercises/4.01-non-uniform-random-numbers/) | yes | inverse CDF, hit-and-miss | ⬜ todo |
| 4.2 | [Gaussian RNG](Exercises/4.02-gaussian-rng/) | yes | Box–Muller | ⬜ todo |
| 4.3 | [Monte Carlo integration (I)](Exercises/4.03-mc-integration-1/) | yes | importance sampling, $\sigma^2\sim 1/N$ | ⬜ todo |
| 4.4 | [Monte Carlo integration (II)](Exercises/4.04-mc-integration-2-metropolis/) | yes | Metropolis, equilibration | ⬜ todo |
| 4.5 | [Stochastic matrices](Exercises/4.05-stochastic-matrices/) | yes | Markov chains, eigenvalues (analytical) | ⬜ todo |
| 4.6 | [Detailed balance](Exercises/4.06-detailed-balance/) | yes | detailed vs. global balance (analytical) | ⬜ todo |
| 4.7 | [Ising model: uniform sampling](Exercises/4.07-ising-uniform-sampling/) | yes | uniform sampling, hit-and-miss, reweighting | ⬜ todo |
| 4.8 | [Metropolis for the Ising model](Exercises/4.08-ising-metropolis/) | yes | magnetization, autocorrelation, critical slowing down | ⬜ todo |
| 4.9 | [Heat bath for the Potts model](Exercises/4.09-potts-heat-bath/) | one of 4.9–4.11 | heat bath vs. Metropolis | ⬜ todo |
| 4.10 | [Kawasaki: local version](Exercises/4.10-kawasaki-local/) | one of 4.9–4.11 | conserved order parameter | ⬜ todo |
| 4.11 | [Kawasaki: non-local version](Exercises/4.11-kawasaki-nonlocal/) | one of 4.9–4.11 | non-local moves, coarsening | ⬜ todo |
| 4.12 | [Hard disks](Exercises/4.12-hard-disks/) | yes | packing fraction, $g(r)$, cell lists | ⬜ todo |
| 4.13 | [Persistent random walk in continuous time](Exercises/4.13-persistent-random-walk-continuous-time/) | yes | continuous-time MC, first passage | ⬜ todo |
| 4.14 | [Birth–annihilation process](Exercises/4.14-birth-annihilation/) | yes | Gillespie, extinction times | ⬜ todo |
| 4.15 | [Lotka–Volterra model](Exercises/4.15-lotka-volterra/) | yes | Gillespie, predator–prey, absorbing states | ⬜ todo |
| 4.16 | [Brusselator](Exercises/4.16-brusselator/) | yes | Gillespie, limit cycle | ⬜ todo |

Status legend: ⬜ todo | 🟨 in progress | ✅ done (in report)

## Repository structure

```
Coursenotes/            course notes, slides and exam instructions
Exercises/
  4.XX-short-name/
    README.md           question, relevant topics, links, deliverables, results log
    *.py / *.ipynb      simulation code
    figures/            generated plots for the report
report/                 LaTeX source of the report, KU Leuven template (see report/README.md)
CLAUDE.md               instructions for Claude Code (AI assistant) in this repo
```

## Setup

Code is written in Python 3:

```bash
pip install numpy scipy matplotlib numba
```

Each exercise is self-contained; run the scripts from inside the exercise folder.
Random seeds are fixed so results are reproducible.
