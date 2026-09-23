# Module 11 — Deployment, CI/CD & Capstone

## Goal

Ship a complete AI system and prove it can be maintained.

## Deployment skills

- Docker
- non-root containers
- environment-based configuration
- CI test gates
- image builds
- managed container platforms
- database migrations
- secrets management
- rollback plans
- staging vs production

## CI pipeline

At minimum:

```text
push / pull request
    ↓
lint + unit tests
    ↓
eval suite
    ↓
security checks
    ↓
build container
    ↓
deploy to staging
    ↓
smoke test
    ↓
production approval/deploy
```

## Capstone — Production Knowledge & Action Assistant

### Functional requirements

- ingest private documents
- retrieve relevant evidence
- answer with evidence references
- return a typed response schema
- expose at least two tools
- include one write action requiring approval
- maintain bounded session state
- expose a FastAPI API

### Quality requirements

- at least 40 offline eval cases
- separate retrieval and answer-quality metrics
- deterministic format and security checks
- one calibrated model-based rubric
- regression threshold in CI

### Reliability requirements

- request timeout
- bounded retries
- bounded agent/tool steps
- fallback or graceful degradation
- structured logs
- tracing
- cost accounting

### Security requirements

- secrets outside source code
- per-tool authorization
- least privilege
- prompt-injection tests
- human approval for irreversible actions
- no raw model output to shell/SQL/eval

### Deployment requirements

- Docker image
- health/readiness endpoints
- CI workflow
- staging deployment plan
- rollback procedure

## Graduation interview

Be able to answer:

1. Why is this an agent rather than a workflow?
2. What is the largest source of error in your RAG system?
3. What happens when retrieval returns nothing useful?
4. What prevents prompt injection from causing privileged actions?
5. How do you know a model or prompt upgrade is better?
6. What does one request cost at p50 and p95?
7. What happens if the provider is down?
8. How would you investigate one bad production response?
