# Module 03 — Prompting, Structured Output & Tool Schemas

## Goal

Make model output dependable enough for software to consume.

## Learn

- instruction hierarchy
- few-shot examples
- schema-constrained output
- Pydantic / JSON Schema validation
- repair vs retry
- function/tool schemas
- typed error handling
- prompt versioning
- avoiding brittle regex parsing

## Labs

1. Extract invoice fields into a typed schema.
2. Build a lead-classification endpoint that returns a validated enum and confidence rationale.
3. Force malformed outputs in tests and verify your application fails safely.
4. Version two prompts and compare them on the same eval set.

## Anti-pattern

Do not ask a model to return "valid JSON" and then hope. Use a schema-aware mechanism where the provider or framework supports it, and still validate at the application boundary.

## Done when

Every model output consumed by code has a schema and a failure path.
