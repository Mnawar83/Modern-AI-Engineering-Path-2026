from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class EvalCase:
    name: str
    prompt: str
    must_contain: tuple[str, ...] = ()


@dataclass(frozen=True)
class EvalResult:
    name: str
    passed: bool
    output: str
    failures: tuple[str, ...]


def run_case(case: EvalCase, system_under_test: Callable[[str], str]) -> EvalResult:
    output = system_under_test(case.prompt)
    failures = tuple(term for term in case.must_contain if term.lower() not in output.lower())
    return EvalResult(
        name=case.name,
        passed=not failures,
        output=output,
        failures=failures,
    )


def pass_rate(results: list[EvalResult]) -> float:
    if not results:
        return 0.0
    return sum(r.passed for r in results) / len(results)
