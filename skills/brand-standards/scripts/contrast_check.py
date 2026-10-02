#!/usr/bin/env python3
"""WCAG 2.2 contrast and colour-vision checks.

Usage:
    contrast_check.py FG BG [FG BG ...]          # pairs, e.g. "#ffffff" "#0f6e7a"
    contrast_check.py --matrix C1 C2 C3 ...      # every colour against every other
    contrast_check.py --cvd C1 C2 C3 ...         # simulate CVD and flag confusable pairs
    contrast_check.py ... --use body|large|ui    # exit 1 if any pair fails that use
    contrast_check.py ... --json

Thresholds (WCAG 2.2): body text 4.5:1 (AA) / 7:1 (AAA); large text (>= 24px, or
>= 18.66px bold) 3:1 / 4.5:1; UI components and meaningful graphics 3:1 (SC 1.4.11).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import brandlib as bl  # noqa: E402


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("colours", nargs="+")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--matrix", action="store_true")
    mode.add_argument("--cvd", action="store_true")
    ap.add_argument("--use", choices=["body", "large", "ui"], help="Fail (exit 1) if any pair is below this use's threshold")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    try:
        colours = [bl.normalize_hex(c) for c in args.colours]
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.cvd:
        sims = {c: {k: bl.simulate_cvd(c, k) for k in bl.CVD_KINDS} for c in colours}
        issues = bl.cvd_pair_report({c: c for c in colours})
        if args.json:
            print(json.dumps({"simulations": sims, "issues": issues}, indent=2))
        else:
            for c, s in sims.items():
                print(c, " ".join(f"{k}={v}" for k, v in s.items()))
            for i in issues:
                print(f"RISK  {i['pair'][0]} vs {i['pair'][1]}: {i['vision']} (ΔE {i['deltaE']})")
            if not issues:
                print("No confusable pairs found.")
        return 0

    if args.matrix:
        pairs = [(a, b) for a in colours for b in colours if a != b]
    else:
        if len(colours) % 2:
            print("error: give colours as FG BG pairs (or use --matrix)", file=sys.stderr)
            return 2
        pairs = list(zip(colours[::2], colours[1::2]))

    results = [{"fg": fg, "bg": bg, **bl.wcag_report(fg, bg)} for fg, bg in pairs]
    failed = [r for r in results if args.use and r["ratio"] < bl.THRESHOLDS[args.use]]
    if args.json:
        print(json.dumps({"results": results, "failed": failed}, indent=2))
    else:
        print(f"{'FG':8} {'BG':8} {'Ratio':>6}  Rating")
        for r in results:
            print(f"{r['fg']:8} {r['bg']:8} {r['ratio']:>6}  {r['rating']}")
        if args.use:
            print(f"\n{len(failed)} pair(s) below the {args.use} threshold of {bl.THRESHOLDS[args.use]}:1")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
