#!/usr/bin/env python3
"""Compile the report (Windows, Linux, macOS).

Usage (from anywhere):
    python report/build.py            build main.pdf once, then clean auxiliary files
    python report/build.py --watch    rebuild automatically whenever a source file changes
    python report/build.py --clean    only remove auxiliary files
    python report/build.py --keep     build once, keep auxiliary files (faster next build)

Uses latexmk when available (it handles bibtex and the reruns). Otherwise it falls back
to pdflatex + bibtex + pdflatex x2 and, for --watch, polls the source files.
"""

import argparse
import shutil
import subprocess
import sys
import time
from pathlib import Path

REPORT = Path(__file__).resolve().parent
MAIN = "main.tex"
AUX_EXT = [".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk",
           ".synctex.gz", ".bbl", ".blg", ".lof", ".lot"]
WATCH_GLOBS = ["*.tex", "*.sty", "*.bib", "sections/*.tex",
               "../Exercises/*/figures/*.pdf", "../Exercises/*/figures/*.png"]
LATEXMK_FLAGS = ["-pdf", "-interaction=nonstopmode", "-file-line-error"]


def run(cmd):
    print("$", " ".join(cmd), flush=True)
    return subprocess.run(cmd, cwd=REPORT).returncode


def clean():
    for ext in AUX_EXT:
        for f in REPORT.glob("main" + ext):
            f.unlink(missing_ok=True)
    for f in (REPORT / "sections").glob("*.aux"):
        f.unlink(missing_ok=True)


def report_log():
    """Print LaTeX errors and the QA counters from main.log."""
    log = REPORT / "main.log"
    if not log.exists():
        return
    text = log.read_text(encoding="latin-1")
    errors = [l for l in text.splitlines() if l.startswith("!") or ":error:" in l.lower()
              or (".tex:" in l and "error" in l.lower())]
    overfull = text.count("Overfull")
    undefined = text.count("undefined")
    for e in errors[:10]:
        print("  ERROR:", e)
    print(f"  Overfull boxes: {overfull}   'undefined' warnings: {undefined}")


def build_fallback():
    """pdflatex + bibtex + 2x pdflatex, for machines without latexmk."""
    pdflatex = ["pdflatex", "-interaction=nonstopmode", "-file-line-error", MAIN]
    if run(pdflatex) != 0:
        return 1
    if shutil.which("bibtex") and (REPORT / "main.aux").exists():
        run(["bibtex", "main"])
    run(pdflatex)
    return run(pdflatex)


def build_once():
    if shutil.which("latexmk"):
        code = run(["latexmk", *LATEXMK_FLAGS, "-halt-on-error", MAIN])
    elif shutil.which("pdflatex"):
        code = build_fallback()
    else:
        sys.exit("Neither latexmk nor pdflatex found. Install MiKTeX or TeX Live.")
    report_log()
    print("OK: report/main.pdf" if code == 0 else f"FAILED (exit code {code})", flush=True)
    return code


def snapshot():
    files = {p for g in WATCH_GLOBS for p in REPORT.glob(g)}
    return {p: p.stat().st_mtime for p in files if p.exists()}


def watch():
    if shutil.which("latexmk"):
        # -pvc: latexmk keeps running and rebuilds on every change. -view=none: no viewer.
        print("Watching with latexmk -pvc (Ctrl+C to stop) ...")
        try:
            return run(["latexmk", *LATEXMK_FLAGS, "-pvc", "-view=none", MAIN])
        except KeyboardInterrupt:
            return 0
    print("Watching by polling (Ctrl+C to stop) ...")
    last = snapshot()
    build_once()
    try:
        while True:
            time.sleep(1)
            now = snapshot()
            if now != last:
                last = now
                print("\nChange detected, rebuilding ...")
                build_once()
    except KeyboardInterrupt:
        return 0


def main():
    ap = argparse.ArgumentParser(description="Compile the LaTeX report.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--watch", action="store_true", help="rebuild on every change")
    g.add_argument("--clean", action="store_true", help="only remove auxiliary files")
    g.add_argument("--keep", action="store_true", help="keep auxiliary files after building")
    args = ap.parse_args()

    if args.clean:
        clean()
        print("Auxiliary files removed.")
        return 0
    if args.watch:
        return watch()
    code = build_once()
    if not args.keep:
        clean()
    return code


if __name__ == "__main__":
    sys.exit(main())
