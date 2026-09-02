# Extended Introduction to Computer Science - Homework 4

A 2017 CS BSc Python assignment covering higher-order accumulation and composition, three recursive and dynamic-programming formulations of rod cutting, recursive subtraction-game solvers, and multidimensional random-walk statistics.

## Algorithms

- Accumulate values with an element-first binary function and compose a list of functions from right to left.
- Compare direct recursion, memoization, and bottom-up dynamic programming for unbounded rod cutting.
- Determine winning subtraction-game positions with direct and memoized recursion.
- Simulate diagonal lattice walks and aggregate distance and origin-return statistics.

## Setup

```bash
git clone https://github.com/KobieHazon/bsc-extended-intro-cs-hw4.git
cd bsc-extended-intro-cs-hw4
uv sync --dev
```

The maintained package supports Python 3.10 or newer and has no runtime dependencies.

## Usage

```bash
uv run extended-intro-hw4 rod-profit 4 1,5,8,9
uv run extended-intro-hw4 winning-position 20 1,2,3,4
uv run extended-intro-hw4 walk-stats 100 2 --runs 1000 --seed 2024
```

The first two commands print `10` and `False`. Random-walk commands use an explicit seed so the reported experiment can be repeated.

## Testing

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

The tests cover function-order semantics, all rod-cutting and game-solving variants, invalid inputs, deterministic walk statistics, command-line behavior, and the complete supplied tester. The untouched recovered solution passes both its embedded checks and the supplied tester before modernization.

## Repository Structure

- `assignment/hw4_tester.py`: supplied tester preserved in its original form
- `assignment/score-key.pdf`: supplied grading key
- `assignment/general-notes.pdf`: supplied general feedback and algorithm notes
- `solution/written-answers.pdf`: my ten-page written submission with identifying metadata reduced to the author's name
- `src/extended_intro_hw4/`: maintained algorithms and command-line interface
- `tests/`: portable pytest regression suite, including the supplied tester

## Implementation notes

The recovered source combines my implementations with the distributed scaffold. Scaffold comments remain in the historical solution commit and are not presented as authored work.

## Experiment Scope

Each random-walk step changes every coordinate independently by either minus one or plus one, matching the recovered exercise rather than a single-axis lattice walk. The resulting statistics are simulation estimates, not analytical guarantees. Reported results must include the run length, dimensionality, number of runs, and random seed.

## License

No repository-wide license is declared because the repository combines original work with supplied material whose reuse terms were not recorded.
