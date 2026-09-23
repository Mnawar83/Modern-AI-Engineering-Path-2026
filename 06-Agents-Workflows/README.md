# Module 06 — Tools, Workflows & Agents

## Goal

Build action-taking AI systems while keeping control flow understandable and bounded.

## Learn

- function/tool calling
- tool descriptions and schemas
- deterministic workflows
- state machines and graphs
- agent loops
- memory and session state
- planning vs execution
- multi-agent patterns
- human-in-the-loop
- retries and idempotency
- step, token, time and cost budgets

## Framework options

Learn the concepts first. Then implement them with one framework, such as:

- LangGraph for explicit graph/state-machine control
- OpenAI Agents SDK for lightweight agent/tool/handoff workflows
- a custom loop when your requirements are simple

## Decision rule

Use:

- **one model call** when one call is enough
- **a workflow** when you know the steps
- **an agent** when the model genuinely needs to choose the next step dynamically

## Labs

1. Build a two-tool assistant.
2. Rebuild it as an explicit deterministic workflow.
3. Rebuild it as an agent and compare complexity.
4. Add maximum tool calls and maximum runtime.
5. Add human approval before one write action.
6. Simulate a tool timeout and a duplicate retry.

## Done when

You can justify why a system needs an agent instead of using "agent" as a default architecture.
