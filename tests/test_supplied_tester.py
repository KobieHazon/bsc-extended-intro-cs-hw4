from __future__ import annotations

import threading
import warnings
from pathlib import Path

import extended_intro_hw4

REPOSITORY_ROOT = Path(__file__).parents[1]


def test_maintained_implementation_passes_supplied_tester(monkeypatch) -> None:
    monkeypatch.setattr(threading.Thread, "isAlive", threading.Thread.is_alive, raising=False)
    namespace = {name: getattr(extended_intro_hw4, name) for name in extended_intro_hw4.__all__}
    tester = REPOSITORY_ROOT / "assignment/hw4_tester.py"

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", SyntaxWarning)
        warnings.simplefilter("ignore", DeprecationWarning)
        exec(compile(tester.read_text(encoding="utf-8"), str(tester), "exec"), namespace)

    assert namespace["test_results"] == ["0"]
