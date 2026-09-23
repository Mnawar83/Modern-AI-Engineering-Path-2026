# Module 04 — Embeddings, Retrieval & Production RAG

## Goal

Build retrieval systems you can diagnose, not just demo.

## Learn

- embeddings and vector similarity
- chunking strategies
- metadata filters
- vector stores
- hybrid search
- reranking
- context assembly
- citations / evidence grounding
- retrieval metrics
- freshness and re-indexing
- permissions-aware retrieval

## Architecture

```text
documents → parse → chunk → enrich metadata → embed → index
                                                ↓
question → query transform → retrieve → rerank → context → model → answer
```

## Labs

1. Compare three chunk sizes on the same document set.
2. Evaluate top-k retrieval before generating any answer.
3. Add metadata filtering by tenant/user/document type.
4. Add reranking and measure whether it improves retrieval quality.
5. Make answers return evidence references.
6. Create a deliberately adversarial document containing prompt injection and test that retrieved text is treated as data, not trusted instructions.

## Metrics

Measure retrieval separately from generation. Useful concepts include:

- Recall@k
- Precision@k
- MRR
- hit rate
- answer groundedness
- citation correctness

## Done when

When an answer is bad, you can determine whether the failure came from parsing, chunking, retrieval, reranking, context construction or generation.
