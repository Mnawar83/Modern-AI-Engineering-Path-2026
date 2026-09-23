# Module 05 — Evals, Testing & Regression Control

## Goal

Turn subjective "this prompt feels better" iteration into measured engineering.

## Learn

- task-specific eval datasets
- golden cases and edge cases
- deterministic checks
- rubric-based grading
- model-based judges and their limitations
- pairwise comparison
- retrieval evals vs generation evals
- regression thresholds
- online vs offline evaluation
- human review sampling

## The core loop

```text
change → run evals → inspect failures → decide → deploy → monitor → add new failures to eval set
```

## Labs

1. Create 30 representative cases for one AI task.
2. Add deterministic validators for format, prohibited fields and required citations.
3. Add one model-based rubric judge.
4. Compare two prompts without changing the dataset.
5. Make CI fail when quality drops below your chosen threshold.

## Warning

An LLM judge is a measurement tool, not ground truth. Calibrate it against human labels and keep deterministic checks wherever possible.

## Done when

You refuse to ship a prompt or model change based only on anecdotal examples.
