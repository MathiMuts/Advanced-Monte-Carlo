# CLAUDE.md

Guidance for Claude when working in this repository.

## Purpose

This repo holds my solutions to the exercises (Chapter 4, "Problems") of the course
**Advanced Monte Carlo Simulations** (Prof. Enrico Carlon). Your job is to help me
*make* the exercises: understand the theory, write and debug the simulation code,
produce the plots, and prepare for the oral exam where I have to explain everything
myself. Act as a tutor and collaborator, not a solution dispenser: explain the *why*
(physics, algorithm, statistics) along with the *what*, so I can defend it at the exam.

## Repository layout

```
Coursenotes/
  monte_carlo_2025.pdf   # lecture notes (51 p.) - the main reference, problems in Ch. 4 (p. 31-48)
  MCarlo-2024.pdf        # handwritten lecture slides (2024), mostly figures, little extractable text
  exam.txt               # assignment + exam instructions (read this for requirements)
Exercises/
  4.XX-short-name/
    README.md            # question, topics, links, deliverables, notes, results log
    *.py / *.ipynb       # code for that exercise
    figures/             # generated plots (png/pdf) used in the report
README.md                # global overview + progress table
```

Each exercise folder corresponds to exactly one problem from Chapter 4 of the notes.
When adding code or results, keep them inside that exercise's folder.

## Assignment requirements (from `Coursenotes/exam.txt`)

- **Required:** 4.1-4.8 and 4.12-4.16.
- **At least one of:** 4.9, 4.10, 4.11.
- Deliverables: a single PDF report (~25 pages) with graphs + short explanatory text,
  uploaded to Toledo at least one day before the exam, plus the code (separate Toledo assignment).
- Every plot: clearly identified quantities, labelled axes, and the simulation details
  (parameters, number of samples/sweeps, seeds, equilibration time, ...).
- The report must end with a statement on what AI was used for.
- Exam: closed-book written theory part, then a 15-20 min oral on the report and code.

## Working conventions

- **Language:** Python 3 with `numpy`, `matplotlib` (and `scipy` for fits). Use `numba`
  for the hot loops of lattice/particle simulations (Ising, Potts, Kawasaki, hard disks)
  when plain numpy is too slow. Ask before introducing other dependencies.
- **Reproducibility:** use `rng = np.random.default_rng(seed)` with an explicit seed;
  never the legacy global `np.random.*` state. Put all parameters at the top of a script
  (or in a config cell) so they can be quoted in the report.
- **Plots:** labelled axes with units/symbols, legend, and a title or caption string listing
  the parameters. Save to the exercise's `figures/` folder as both `.png` and `.pdf`.
  Use LaTeX-style labels (`r"$\beta$"`) and keep a consistent style across exercises.
- **Statistics:** always report error bars (standard error, or blocking/binning analysis
  for correlated Markov-chain data, taking the autocorrelation time into account).
  Discard the equilibration period before measuring.
- **Performance tricks from the notes:** precompute the Boltzmann factors
  (only a few discrete $\Delta E$ values for Ising/Potts), compute $\Delta E$ locally from
  nearest neighbours, reuse the last configuration when sweeping in temperature.
- **Time units:** one Monte Carlo sweep = one attempted update per spin/particle.
- Keep code readable and commented enough that I can explain it at the oral exam;
  prefer clarity over cleverness.

## Reading the course notes

`pdftotext` garbles most of the equations in `monte_carlo_2025.pdf`. When the exact form
of an equation matters, read the relevant page(s) with the Read tool and the `pages`
parameter (printed page numbers equal PDF page numbers). Each exercise README lists the
pages of the problem and of the related theory sections.

## When helping with an exercise

1. Read that exercise's `README.md` (and the notes pages it links) first.
2. For analytical sub-questions, guide me through the derivation; write it in the README
   (Markdown + `$...$` math) or in LaTeX for the report.
3. For simulation sub-questions, write/modify code in the exercise folder, run it, and
   check results against known values (exact solutions, analytical limits) where possible.
4. Update the README: tick off the sub-question checkboxes, fill in "Results & notes",
   and add a line to the "AI usage log" describing what you helped with (needed for the
   AI statement in the report).
5. Update the progress table in the root `README.md` when an exercise's status changes.

Do not commit or push unless I ask.
