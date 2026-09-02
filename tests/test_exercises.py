import random

import pytest

from extended_intro_hw4 import (
    acc,
    compose,
    myProd,
    profit,
    profit2,
    profit3,
    rw_stats,
    walk,
    win,
    win2,
)


def test_acc_preserves_element_first_order() -> None:
    assert acc(lambda value, result: value - result, 10, [1, 2, 3]) == -8
    assert acc(lambda left, right: left ^ right, 0, [13, 24, 57, 63]) == 19


def test_product_and_empty_assignment_behavior() -> None:
    assert myProd([1, 2, 3, 4, 5]) == 120
    assert myProd([]) == 0


def test_compose_applies_last_function_first() -> None:
    function = compose([lambda value: value**2, lambda value: value + 6, lambda value: value / 2])
    assert function(10) == 121
    assert compose([])(10) == 10


@pytest.mark.parametrize("function", [profit, profit2, profit3])
@pytest.mark.parametrize(
    ("values", "size", "expected"),
    [([1, 5, 8, 9], 4, 10), ([1, 2, 7, 8, 9, 12, 13], 6, 14), ([2, 3, 5, 7], 0, 0)],
)
def test_rod_cutting_variants(function, values: list[int], size: int, expected: int) -> None:
    assert function(values, size) == expected


@pytest.mark.parametrize("function", [profit, profit2, profit3])
def test_rod_cutting_requires_complete_prices(function) -> None:
    with pytest.raises(ValueError):
        function([1, 3], 3)


@pytest.mark.parametrize("function", [win, win2])
@pytest.mark.parametrize(
    ("number", "moves", "expected"),
    [(9, [1], True), (10, [1], False), (20, [1, 2, 3, 4, 5], True), (15, [1, 2, 7], False)],
)
def test_subtraction_game(function, number: int, moves: list[int], expected: bool) -> None:
    assert function(number, moves) is expected


def test_subtraction_game_rejects_invalid_moves() -> None:
    with pytest.raises(ValueError):
        win2(5, [0, 2])


def test_random_walk_is_reproducible() -> None:
    assert walk(6, 2, rng=random.Random(7)) == (4.0, False)


def test_random_walk_statistics_are_reproducible() -> None:
    assert rw_stats(8, 2, 25, rng=random.Random(2024)) == pytest.approx(
        (8, 3.5521334111185148, 1.255868811340602, 0.0, 8.48528137423857, 0.32)
    )


def test_zero_length_walk_has_defined_normalization() -> None:
    assert rw_stats(0, 3, 2, rng=random.Random(1)) == (0, 0.0, 0.0, 0.0, 0.0, 0.0)
