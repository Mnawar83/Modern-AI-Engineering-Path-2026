# Module 02 — LLM Fundamentals & APIs

## Goal

Use modern language models as programmable components rather than chat interfaces.

## Learn

- tokens and context windows
- system/developer/user instructions
- sampling and determinism
- reasoning vs output verbosity
- streaming
- request timeouts and retries
- multimodal inputs
- provider abstraction and model portability
- cost accounting
- prompt caching where supported

## Labs

1. Build the same classifier with two different model providers.
2. Stream a response to the terminal.
3. Measure input tokens, output tokens, latency and estimated cost per request.
4. Add timeout, retry and fallback behavior.
5. Send text plus an image to a multimodal model and extract facts.

## Engineering rule

Wrap providers behind your own small application interface. Avoid scattering provider-specific calls across the codebase.

## Done when

You can swap the underlying model without rewriting your product logic.
