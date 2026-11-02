#!/usr/bin/env python3
"""lab_doctor.py - pre-flight check for a department of one.

Run this before starting a lab (or any project). It verifies the
environment the department depends on, and says exactly what is
missing. A WARN is workable; a FAIL will bite later today.

Usage:  python lab_doctor.py [project-folder]   (default: current folder)
"""

import shutil
import subprocess
import sys
from pathlib import Path

MIN_PYTHON = (3, 8)


def check(name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {name}" + (f" - {detail}" if detail else ""))
    return ok


def warn(name, detail=""):
    print(f"  [WARN] {name}" + (f" - {detail}" if detail else ""))


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    print(f"Lab doctor - checking {root}\n")
    failures = 0

    # Python itself
    version = sys.version_info
    failures += 0 if check(f"Python {version.major}.{version.minor}",
                           version >= MIN_PYTHON,
                           "" if version >= MIN_PYTHON else f"need 3.8+, found {version}") else 1

    # Git installed
    git = shutil.which("git")
    if not check("git installed", git is not None):
        failures += 1

    # Git repository initialised here
    if (root / ".git").is_dir():
        check("git repository initialised", True)
    else:
        warn("git repository not initialised here", "run: git init")
        warn("everything in this folder is currently unrecorded")

    # An agent configuration file (context folder front door)
    agents = [p for p in root.glob("AGENT*.*") if not p.name.startswith("._")]
    if agents:
        check(f"agent briefing present ({agents[0].name})", True)
    else:
        warn("no AGENTS.md found", "the intern starts every chat from zero")

    # Evidence trio present?
    trio = [p.name for p in root.iterdir()
            if p.name.lower() in ("spec.md", "decisions.md", "critique.md")]
    if trio:
        check(f"evidence trio files found ({len(trio)}/3)", True)
    else:
        warn("no evidence trio files (SPEC/DECISIONS/CRITIQUE)",
             "fine before Lab 3; expected after")

    # The quality gate, if the project has adopted it
    gate = root / "slop_check.py"
    if gate.is_file():
        check("slop gate present (slop_check.py)", True)
    else:
        warn("no slop gate (slop_check.py)", "adopt it once tests exist (Ch 9 / Lab 13)")

    # Model credits are the one thing we cannot probe - ask instead
    print("  [ASK ] model access: is your agent authenticated and funded?")

    print()
    if failures:
        print(f"NOT READY - {failures} failure(s) to fix before starting.")
        sys.exit(1)
    print("Environment ready. Brief the department.")


if __name__ == "__main__":
    main()
