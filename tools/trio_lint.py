#!/usr/bin/env python3
"""trio_lint.py - the evidence trio linter.

Checks that the three documents of a spec-first project exist and
carry the content the Replication Test depends on:

  SPEC.md       exists, non-trivial, has a "done means" section
  DECISIONS.md  exists, has dated entries
  CRITIQUE.md   exists, has a position and a reason

Usage:  python trio_lint.py [project-folder]     (default: current folder)

Exit 0 = trio is healthy. Exit 1 = findings, listed below.
"""

import re
import sys
from pathlib import Path

MIN_SPEC_LINES = 6
MIN_BODY_CHARS = 80


def find(names, root):
    """Case-insensitive lookup for the first matching file."""
    for name in names:
        hit = root / name
        if hit.is_file():
            return hit
    lower = {p.name.lower(): p for p in root.iterdir() if p.is_file()}
    for name in names:
        if name.lower() in lower:
            return lower[name.lower()]
    return None


def lint(root):
    findings = []

    # --- SPEC.md ---
    spec = find(["SPEC.md", "Spec.md", "spec.md"], root)
    if not spec:
        findings.append("SPEC.md missing - the Replication Test has nothing to run")
    else:
        text = spec.read_text(encoding="utf-8", errors="replace")
        if len(text.strip().splitlines()) < MIN_SPEC_LINES:
            findings.append("SPEC.md is thinner than a stranger could build from")
        if not re.search(r"done\s*means", text, re.I):
            findings.append('SPEC.md has no "Done means" section - done is undefined')
        if re.search(r"\b(nice|clean|user-friendly|robust)\b", text, re.I):
            hits = re.findall(r"\b(nice|clean|user-friendly|robust)\b", text, re.I)
            findings.append(
                "SPEC.md uses untestable words (" + ", ".join(sorted(set(hits)))
                + ") - replace each with the example that settles it")

    # --- DECISIONS.md ---
    decisions = find(["DECISIONS.md", "Decisions.md", "decisions.md"], root)
    if not decisions:
        findings.append("DECISIONS.md missing - decisions live in someone's memory")
    else:
        text = decisions.read_text(encoding="utf-8", errors="replace")
        dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)
        if not dates:
            findings.append("DECISIONS.md has no dated entries - undated decisions decay")
        rows = [l for l in text.splitlines() if l.strip().startswith("|")]
        if len(rows) < 2:
            findings.append("DECISIONS.md looks empty of decisions (table or dated list expected)")

    # --- CRITIQUE.md ---
    critique = find(["CRITIQUE.md", "Critique.md", "critique.md"], root)
    if not critique:
        findings.append("CRITIQUE.md missing - no recorded position, no recorded taste")
    else:
        text = critique.read_text(encoding="utf-8", errors="replace")
        if len(text.strip()) < MIN_BODY_CHARS:
            findings.append("CRITIQUE.md is too thin to be arguable")
        if not re.search(r"why|because|give[sd]? up|change my mind", text, re.I):
            findings.append("CRITIQUE.md has a position but no reason - add the why")

    return findings


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    if not root.is_dir():
        print(f"Not a folder: {root}")
        sys.exit(1)

    print(f"Evidence trio lint: {root}\n")
    findings = lint(root)

    if findings:
        print("FINDINGS:")
        for finding in findings:
            print(" -", finding)
        print(f"\n{len(findings)} finding(s). Fix them, then re-run.")
        sys.exit(1)

    print("Trio healthy: SPEC with done-means, dated decisions, arguable critique.")


if __name__ == "__main__":
    main()
