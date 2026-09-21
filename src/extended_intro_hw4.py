"""Maintained implementations of the Homework 4 programming questions."""

from __future__ import annotations

import math
import random
from collections.abc import Callable, Sequence
from functools import lru_cache
from typing import TypeVar

__all__ = [
    "acc",
    "compose",
    "g",
    "h",
    "myProd",
    "profit",
    "profit2",
    "profit3",
    "rw_stats",
    "walk",
    "win",
    "win2",
]

T = TypeVar("T")
R = TypeVar("R")


def acc(function: Callable[[T, R], R], initial: R, values: Sequence[T]) -> R:
    """Accumulate left to right using the assignment's element-first argument order."""
    result = initial
    for value in values:
        result = function(value, result)
    return result


def myProd(values: Sequence[int | float]) -> int | float:
    """Return the product of a non-empty sequence, or zero for an empty sequence."""
    if not values:
        return 0
    return acc(lambda value, result: value * result, 1, values)


def g(first: Callable[[T], R], second: Callable[[R], T]) -> Callable[[T], T]:
    """Compose two functions as ``second(first(value))``."""
    return lambda value: second(first(value))


def h(value: T) -> T:
    """Return the identity value."""
    return value


def compose(functions: Sequence[Callable[[T], T]]) -> Callable[[T], T]:
    """Compose functions so the last listed function is applied first."""

    def composed(value: T) -> T:
        result = value
        for function in reversed(functions):
            result = function(result)
        return result

    return composed


def profit(values: Sequence[int], size: int) -> int:
    """Solve unbounded rod cutting with direct recursion."""
    _validate_prices(values, size)
    if size == 0:
        return 0
    return max(values[length - 1] + profit(values, size - length) for length in range(1, size + 1))


def profit2(values: Sequence[int], size: int) -> int:
    """Solve unbounded rod cutting with top-down memoization."""
    _validate_prices(values, size)

    @lru_cache(maxsize=None)
    def solve(remaining: int) -> int:
        if remaining == 0:
            return 0
        return max(
            values[length - 1] + solve(remaining - length) for length in range(1, remaining + 1)
        )

    return solve(size)


def profit3(values: Sequence[int], size: int) -> int:
    """Solve unbounded rod cutting with bottom-up dynamic programming."""
    _validate_prices(values, size)
    best = [0] * (size + 1)
    for remaining in range(1, size + 1):
        best[remaining] = max(
            values[length - 1] + best[remaining - length] for length in range(1, remaining + 1)
        )
    return best[size]


def win(number: int, moves: Sequence[int]) -> bool:
    """Return whether the current player can win the subtraction game recursively."""
    normalized_moves = _validate_game(number, moves)
    if number == 0:
        return False
    return any(
        move == number or (move < number and not win(number - move, normalized_moves))
        for move in normalized_moves
    )


def win2(number: int, moves: Sequence[int]) -> bool:
    """Return whether the current player can win using memoized recursion."""
    normalized_moves = _validate_game(number, moves)

    @lru_cache(maxsize=None)
    def solve(remaining: int) -> bool:
        return any(
            move == remaining or (move < remaining and not solve(remaining - move))
            for move in normalized_moves
        )

    return solve(number)


def walk(
    run_length: int,
    dimensions: int,
    *,
    rng: random.Random | None = None,
) -> tuple[float, bool]:
    """Run a diagonal lattice walk and report final distance and origin return."""
    if run_length < 0:
        raise ValueError("run_length must be non-negative")
    if dimensions < 1:
        raise ValueError("dimensions must be positive")
    generator = rng or random
    location = [0] * dimensions
    returned_to_origin = False
    for _ in range(run_length):
        for coordinate in range(dimensions):
            location[coordinate] += generator.choice((-1, 1))
        returned_to_origin = returned_to_origin or all(value == 0 for value in location)
    distance = math.sqrt(sum(value**2 for value in location))
    return distance, returned_to_origin


def rw_stats(
    run_length: int,
    dimensions: int,
    number_runs: int = 10**3,
    *,
    rng: random.Random | None = None,
) -> tuple[int, float, float, float, float, float]:
    """Aggregate final-distance and origin-return statistics for random walks."""
    if number_runs < 1:
        raise ValueError("number_runs must be positive")
    generator = rng or random
    outcomes = [walk(run_length, dimensions, rng=generator) for _ in range(number_runs)]
    distances = [distance for distance, _returned in outcomes]
    origin_frequency = sum(returned for _distance, returned in outcomes) / number_runs
    normalized_average = sum(distances) / number_runs
    root_normalized = normalized_average / math.sqrt(run_length) if run_length else 0.0
    return (
        run_length,
        normalized_average,
        root_normalized,
        min(distances),
        max(distances),
        origin_frequency,
    )


def _validate_prices(values: Sequence[int], size: int) -> None:
    if size < 0:
        raise ValueError("size must be non-negative")
    if len(values) < size:
        raise ValueError("a price is required for every length through size")


def _validate_game(number: int, moves: Sequence[int]) -> tuple[int, ...]:
    if number < 0:
        raise ValueError("number must be non-negative")
    normalized = tuple(sorted(set(moves)))
    if not normalized or normalized[0] < 1:
        raise ValueError("moves must contain positive integers")
    return normalized
