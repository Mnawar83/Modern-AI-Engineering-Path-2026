# Module 08 — Safety, Security & Human Approval

## Goal

Treat model-controlled execution as an untrusted-input problem.

## Threat model

A user can influence the model. Retrieved content can influence the model. Tool output can influence the model. Therefore model output is not a trusted security boundary.

## Learn

- prompt injection
- indirect prompt injection through retrieved content
- data exfiltration risks
- least-privilege tool design
- allowlists
- sandboxing
- secrets handling
- PII and sensitive-data controls
- authorization at the tool/backend layer
- human approval
- audit logs
- irreversible-action policies

## Rules

- Never pass raw model output into `eval`, `exec` or a shell.
- Never build SQL by concatenating model text.
- Enforce authorization in code, not in the prompt.
- Give tools the minimum permissions necessary.
- Separate read tools from write tools.
- Require approval for money movement, deletion, outbound messages and privileged writes.
- Treat retrieved documents as untrusted data.

## Labs

1. Red-team your RAG system with malicious instructions inside a document.
2. Red-team a tool with out-of-range and unexpected arguments.
3. Add an approval gate around an outbound email or simulated refund.
4. Add tenant-level authorization independent of the model.
5. Verify secrets never appear in traces or logs.

## Done when

You can identify the security boundary of every tool and prove that the model cannot grant itself more authority.
