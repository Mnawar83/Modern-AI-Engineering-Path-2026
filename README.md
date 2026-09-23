# Modern AI Engineering Path — 2026 Edition

A practical, production-oriented learning path for building AI products with modern language models.

This curriculum is designed for people who want to **ship reliable AI applications**, not spend months waiting to reach LLMs after completing a traditional machine-learning syllabus.

## What this path optimizes for

You will learn to:

- call modern model APIs and reason about tokens, context, latency and cost
- get dependable structured output instead of parsing prose
- build retrieval-augmented generation systems and diagnose retrieval failures
- create eval sets and regression tests before prompt changes reach users
- build tool-using agents and know when **not** to use an agent
- connect models to external systems through Model Context Protocol (MCP)
- defend against prompt injection, unsafe tool execution and data leakage
- expose AI features through FastAPI services
- add tracing, metrics, caching, fallbacks and budgets
- package with Docker and ship through CI/CD
- make architecture decisions based on reliability and economics, not hype

## The path

| Module | Focus | Suggested time |
|---|---|---:|
| 00 | Engineering foundations: Python, Git, HTTP, JSON, async, testing | 3–5 days |
| 01 | ML & neural-network foundations, compressed | 3–5 days |
| 02 | LLM fundamentals and model APIs | 1 week |
| 03 | Prompting, structured output and tool schemas | 1 week |
| 04 | Embeddings, retrieval and production RAG | 1–2 weeks |
| 05 | Evals, testing and regression control | 1 week |
| 06 | Tools, workflows and agents | 1–2 weeks |
| 07 | MCP and external systems | 1 week |
| 08 | Safety, security and human approval | 1 week |
| 09 | Production AI services and data layer | 1 week |
| 10 | Observability, cost, latency and reliability | 1 week |
| 11 | Deployment, CI/CD and capstone | 1–2 weeks |

**Recommended total:** about 10–13 weeks part-time.

## The mental model

Modern AI engineering is not mainly about training a foundation model. It is about composing a system around a model:

```text
user
  ↓
application / API
  ↓
validation + policy
  ↓
model call ← retrieval ← data
  ↓             ↓
 tools       embeddings / index
  ↓
external systems
  ↓
validation + eval + logging
  ↓
response
```

The model is one component. Reliability comes from everything around it.

## Two tracks

### Track A — Product AI Engineer

Use this if your goal is SaaS, copilots, agents, workflow automation, internal tools or AI features in existing products.

**Order:** 00 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10 → 11

Do Module 01 alongside the path when you need deeper intuition.

### Track B — ML + AI Engineer

Use this if you also want strong classical ML and deep-learning foundations.

**Order:** 00 → 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10 → 11

## The decision ladder

Before adding complexity, ask:

1. Can a deterministic function solve it?
2. Can one model call solve it?
3. Can structured output solve it?
4. Does the model need private or changing knowledge? Add retrieval.
5. Does it need to take actions? Add tools.
6. Does it need dynamic multi-step control flow? Add an agent or graph.
7. Does the capability need to be reusable across AI hosts? Consider MCP.

Every extra layer adds failure modes, latency and cost.

## Capstone

Build a **Production Knowledge & Action Assistant** that:

- answers questions over a private document set
- cites retrieved evidence
- produces typed/validated responses
- calls at least two safe tools
- requires human approval for one irreversible action
- exposes an API
- includes an eval suite
- logs latency, cost, retrieval quality and tool usage
- handles provider errors and timeouts
- runs in Docker
- passes CI before deploy

See [`11-Deployment-Capstone/README.md`](11-Deployment-Capstone/README.md).

## Repository principles

- **Evals before optimization.** If you cannot measure quality, you cannot improve it.
- **Schemas over prose.** Validate anything another program consumes.
- **Retrieval before fine-tuning for knowledge.** Fine-tuning is usually for behavior, style or task adaptation.
- **Workflows before agents.** Prefer explicit control flow when the steps are known.
- **Human approval before irreversible actions.** Money, deletion, outbound communication and privileged writes deserve gates.
- **Bound every loop.** Time, tokens, retries and tool calls all need limits.
- **Trace everything important.** A demo can be opaque. A production system cannot.
- **Secrets never belong in code, prompts, notebooks or logs.**

## Setup

See [`SETUP.md`](SETUP.md).

## Source note

This curriculum was independently authored as a modernized AI-engineering learning path after reviewing the public repository `moedk2204/AIEngineeringPath`. That repository did not declare a license when reviewed, so this project intentionally avoids copying its source files or substantial instructional text.
