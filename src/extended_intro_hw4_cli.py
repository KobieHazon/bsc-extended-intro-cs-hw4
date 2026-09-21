"""Command-line interface for selected Homework 4 algorithms."""

from __future__ import annotations

import argparse
import random

from extended_intro_hw4 import profit2, rw_stats, win2


def integer_list(value: str) -> list[int]:
    try:
        return [int(item) for item in value.split(",") if item]
    except ValueError as error:
        raise argparse.ArgumentTypeError("values must be comma-separated integers") from error


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    profit_parser = subparsers.add_parser("rod-profit")
    profit_parser.add_argument("size", type=int)
    profit_parser.add_argument("prices", type=integer_list)

    game_parser = subparsers.add_parser("winning-position")
    game_parser.add_argument("number", type=int)
    game_parser.add_argument("moves", type=integer_list)

    walk_parser = subparsers.add_parser("walk-stats")
    walk_parser.add_argument("run_length", type=int)
    walk_parser.add_argument("dimensions", type=int)
    walk_parser.add_argument("--runs", type=int, default=1000)
    walk_parser.add_argument("--seed", type=int, default=2024)
    return parser


def cli() -> None:
    arguments = build_parser().parse_args()
    try:
        if arguments.command == "rod-profit":
            result = profit2(arguments.prices, arguments.size)
        elif arguments.command == "winning-position":
            result = win2(arguments.number, arguments.moves)
        else:
            result = rw_stats(
                arguments.run_length,
                arguments.dimensions,
                arguments.runs,
                rng=random.Random(arguments.seed),
            )
        print(result)
    except ValueError as error:
        raise SystemExit(f"error: {error}") from error


if __name__ == "__main__":
    cli()
