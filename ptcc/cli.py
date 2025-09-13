# ptcc/cli.py

"""
ptcc.cli

Provides a command-line interface to the ptcc package.
"""

import argparse
import sys

from .cleaner import remove_pytest_cache


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Remove all `.pytest_cache` folders in the given directory tree.",
        add_help=False,
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Root directory to clean (default: current directory)",
    )
    parser.add_argument(
        "-h",
        "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="show this help message and exit",
    )
    args = parser.parse_args()

    removed = remove_pytest_cache(args.path)
    print(f"Removed {removed} `.pytest_cache` folder(s).")

    sys.exit(0 if removed >= 0 else 1)
