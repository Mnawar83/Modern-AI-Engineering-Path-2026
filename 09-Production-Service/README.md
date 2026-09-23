# Module 09 — Production AI Services & Data Layer

## Goal

Turn experiments into maintainable services.

## Learn

- FastAPI application structure
- request and response schemas
- service layers
- dependency injection
- async I/O
- persistence
- queues/background jobs
- idempotency
- authentication
- rate limiting
- tenant isolation
- configuration
- migrations
- health/readiness endpoints

## Recommended structure

```text
src/app/
  api/
  schemas/
  services/
  providers/
  retrieval/
  tools/
  evals/
  security/
  observability/
```

Keep model/provider logic behind interfaces. Routes should be thin.

## Labs

1. Wrap one AI feature in FastAPI.
2. Add an authenticated endpoint.
3. Persist conversations or jobs.
4. Add an idempotency key to a write action.
5. Move one slow task to a background worker design.
6. Add `/health` and `/ready` endpoints with meaningful checks.

## Done when

Your AI feature can run without a notebook and another developer can understand where each responsibility lives.
