# Report

LaTeX source of the exam report: solutions and simulation results for the problems of
Chapter 4 of the lecture notes. Written in the **KU Leuven template** (`kultem.sty`,
skill `kul-template`, alias *kul latex / kul style / kul verslag / kul report*). It has a
cover page with the sedes watermark, blue header and footer bands with the logo, and
sans-serif text and math.

## Requirements (from [`exam.txt`](../Coursenotes/exam.txt))

- Single PDF, roughly 25 pages, uploaded to Toledo at least one day before the exam.
- Graphs with brief explanatory text; all plotted quantities identified, axes labelled.
- For every simulation: parameters, number of samples/sweeps, equilibration, and any other
  detail needed to interpret the results.
- End with a statement on what AI was used for.

## Structure

```
report/
  main.tex              class + kultem, title page fields, TOC, \input of all sections, bibliography
  preamble.tex          extra packages and report macros (loaded after kultem)
  kultem.sty            KU Leuven style (copied from the skill, do not edit)
  img/                  KU Leuven logo + sedes (needed by kultem.sty)
  References.bib        lecture notes, Gillespie (1977), ...
  build.py              build / watch / clean script (cross-platform)
  sections/
    00-introduction.tex             conventions, tools, where the code is
    4.01-....tex ... 4.16-....tex   one file per problem (same names as Exercises/)
    99-ai-statement.tex             required AI statement
  main.pdf              compiled report
```

Each `sections/4.XX-*.tex` file belongs to the folder with the same name in
[`../Exercises/`](../Exercises/). That folder's README has the question, the checklist and
the list of plots the section needs.

## Building

Use `build.py` (Python 3, works on Windows, Linux and macOS, from any directory):

```bash
python report/build.py            # build main.pdf once, then remove auxiliary files
python report/build.py --watch    # rebuild automatically on every change (Ctrl+C to stop)
python report/build.py --keep     # build once, keep auxiliary files (faster rebuilds)
python report/build.py --clean    # only remove auxiliary files
```

After each build the script prints any LaTeX errors and the number of overfull boxes.
It uses `latexmk` when available; `--watch` then runs `latexmk -pvc`, which rebuilds when a
file's *content* changes (a plain `touch` does nothing). Without latexmk it falls back to
`pdflatex` + `bibtex` + `pdflatex` ×2 and polls the sources (including the exercise
figures) once per second.

Manual equivalent: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.

Build with pdflatex (MiKTeX installs the missing packages on demand: cmbright, iwona,
sansmath, stackengine, background, ...). Build files are ignored by `.gitignore`. `main.pdf` is kept.

## Conventions

### Numbering

Sections are numbered like the problems in the notes. Start each problem with
`\exercise{n}{Title}`, which produces section **4.n** even if earlier optional
problems are left out. Subsections then become 4.n.1, 4.n.2, ... (one per sub-question).
Use `\unnumberedsection{...}` for the introduction and the AI statement.

### Figures

`\graphicspath` points to `../Exercises/` (and `img/`), so include plots by exercise folder:

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\linewidth]{4.08-ising-metropolis/figures/m_vs_t}
  \caption{Magnetization per spin vs.\ MC sweeps, $N=50$, $T=2$, ... (all parameters).}
  \label{fig:4.8-m-vs-t}
\end{figure}
```

Plots come from the Python scripts as PDF (vector) in a sans-serif font, coloured with the
KU Leuven blues (`#1FABD5`, `#1D8DB0`, `#116E8A`). Captions must list the simulation
parameters. Use `subcaption` for side-by-side panels.

### Boxes

There is a single box, `\kulbox[5pt]{...}` (light blue). Use it for the main result of a
problem (fitted $\tau$, $z$, value of $I$, ...) and at most once per page.

### Writing

- No em dashes in prose. Use `--` only for numeric ranges.
- Short paragraphs, one idea each. Display math for important equations.
- Numbers come from the scripts and are never computed by hand. Give 2–3 significant figures, with error bars.
- Cite with `\cite{Carlon2025}` (lecture notes) and `\cite{Gillespie1977}`. Protect capitals in `.bib` titles with braces.
- Shortcut macros: `\Tc`, `\taueq`, `\avg{...}`.

## Checks before submitting

1. Compiles without errors, `grep -c Overfull main.log` = 0.
2. `pdffonts main.pdf | grep -c "Type 3"` = 0.
3. Look over the rendered pages: no orphaned headings, readable figures, labelled axes, the right section in the footer.
4. Every required problem (4.1–4.8, 4.12–4.16) and at least one of 4.9–4.11 is present.
5. The AI statement (`sections/99-ai-statement.tex`) is filled in.
