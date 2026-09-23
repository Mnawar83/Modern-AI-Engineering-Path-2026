from examples.evals.eval_runner import EvalCase, pass_rate, run_case


def test_run_case_passes_required_term() -> None:
    case = EvalCase(name="citation", prompt="Answer", must_contain=("source",))
    result = run_case(case, lambda _: "Answer with source: doc-1")
    assert result.passed


def test_pass_rate() -> None:
    cases = [
        EvalCase(name="a", prompt="a", must_contain=("x",)),
        EvalCase(name="b", prompt="b", must_contain=("y",)),
    ]
    results = [run_case(cases[0], lambda _: "x"), run_case(cases[1], lambda _: "no")]
    assert pass_rate(results) == 0.5
