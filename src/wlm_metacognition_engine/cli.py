"""
Command-line interface for WLM‑Metacognition‑Engine.

Usage:
    wlm-metacognition analyze "If A then B."
    wlm-metacognition analyze input.txt
"""

import argparse
import json
import sys
from pathlib import Path

from .api import analyze_reasoning


def load_input(input_arg: str):
    """
    Load input either from a text file or inline string.
    """
    path = Path(input_arg)
    if path.exists() and path.is_file():
        return path.read_text(encoding="utf-8")
    return input_arg


def cmd_analyze(args):
    try:
        text = load_input(args.input)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    result = analyze_reasoning(text)

    if args.out:
        Path(args.out).write_text(json.dumps(result, indent=2), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


def main():
    parser = argparse.ArgumentParser(
        prog="wlm-metacognition",
        description="WLM‑Metacognition‑Engine CLI"
    )

    sub = parser.add_subparsers(dest="command")

    # analyze
    p_analyze = sub.add_parser(
        "analyze",
        help="Analyze reasoning structure"
    )
    p_analyze.add_argument("input", help="Text file path or inline text")
    p_analyze.add_argument("--out", help="Write output to file")
    p_analyze.set_defaults(func=cmd_analyze)

    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        sys.exit(1)

    args.func(args)
