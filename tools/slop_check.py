#!/usr/bin/env python3
"""slop_check.py - the five-gate quality check. Run before any commit.

Gates:
  1. Style and obvious errors   (ruff check)
  2. Behaviour                  (pytest)
  3. Coverage floor             (pytest --cov=src --cov-fail-under=N)
  4. Forgotten promises         (TODO/FIXME count in tracked files)
  5. Change-size budget         (diff vs main, in lines)

Tune the thresholds below; never remove a gate silently.
"""

import subprocess
import sys

TODO_LIMIT = 5
DIFF_LIMIT = 400
COVERAGE_FLOOR = 80


def run(command):
    """Run a shell command, return (ok, combined output)."""
    result = subprocess.run(command, capture_output=True, text=True)
    return result.returncode == 0, result.stdout + result.stderr


def gate(name, ok, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f" - {detail}" if detail else ""))
    return ok


def main():
    print("Slop check - five gates\n")
    failures = []

    # Gate 1: style and obvious errors
    ok, output = run(["ruff", "check", "."])
    detail = "" if ok else output.strip().splitlines()[-1] if output.strip() else ""
    if not gate("Gate 1  lint (ruff)", ok, detail):
        failures.append("Gate 1")

    # Gate 2: behaviour
    ok, output = run(["pytest", "-q"])
    detail = "" if ok else output.strip().splitlines()[-1] if output.strip() else ""
    if not gate("Gate 2  tests (pytest)", ok, detail):
        failures.append("Gate 2")

    # Gate 3: coverage floor
    ok, output = run(["pytest", "-q", "--cov=src",
                      f"--cov-fail-under={COVERAGE_FLOOR}"])
    detail = "" if ok else output.strip().splitlines()[-1] if output.strip() else ""
    if not gate(f"Gate 3  coverage floor ({COVERAGE_FLOOR}%)", ok, detail):
        failures.append("Gate 3")

    # Gate 4: forgotten promises (tracked files only)
    ok, output = run(["git", "grep", "-c", "-E", r"TODO|FIXME"])
    todos = 0
    if ok:
        for line in output.splitlines():
            if ":" in line:
                try:
                    todos += int(line.rsplit(":", 1)[1])
                except ValueError:
                    pass
    if not gate(f"Gate 4  forgotten promises (<={TODO_LIMIT} TODO/FIXME)",
                todos <= TODO_LIMIT, f"count {todos}"):
        failures.append("Gate 4")

    # Gate 5: change-size budget (lines changed vs main)
    ok, output = run(["git", "diff", "main", "--stat"])
    changed = 0
    last = [l for l in output.splitlines() if l.strip()]
    if last and "changed" in last[-1]:
        try:
            numbers = [int(tok) for tok in last[-1].replace(",", "").split()
                       if tok.isdigit()]
            changed = sum(numbers[:-1])  # final number is "files changed"
        except ValueError:
            changed = 0
    if not gate(f"Gate 5  change-size budget (<={DIFF_LIMIT} lines vs main)",
                changed <= DIFF_LIMIT, f"{changed} changed lines"):
        failures.append("Gate 5")

    print()
    if failures:
        print(f"SLOP DETECTED: {len(failures)} gate(s) failed: {', '.join(failures)}")
        sys.exit(1)
    print("All five gates pass.")


if __name__ == "__main__":
    main()
