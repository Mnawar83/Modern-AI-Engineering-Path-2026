from __future__ import annotations

import os
import time
import uuid
from typing import Literal

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="AI Engineering Path Example API", version="0.1.0")


class AskRequest(BaseModel):
    question: str = Field(min_length=1, max_length=4000)


class AskResponse(BaseModel):
    request_id: str
    answer: str
    status: Literal["ok"] = "ok"
    latency_ms: int


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask(payload: AskRequest, x_api_key: str | None = Header(default=None)) -> AskResponse:
    expected = os.getenv("EXAMPLE_API_KEY")
    if expected and x_api_key != expected:
        raise HTTPException(status_code=401, detail="Invalid API key")

    request_id = str(uuid.uuid4())
    started = time.perf_counter()

    # Replace this deterministic placeholder with your model service.
    answer = f"You asked: {payload.question}"

    latency_ms = int((time.perf_counter() - started) * 1000)
    return AskResponse(request_id=request_id, answer=answer, latency_ms=latency_ms)
