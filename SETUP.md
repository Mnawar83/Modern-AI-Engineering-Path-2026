# Setup

## Recommended environment

- Python 3.12+
- Git
- Docker Desktop or Docker Engine
- VS Code or another editor
- `uv` or `pip`

## Create an environment

With `uv`:

```bash
uv venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows PowerShell
uv pip install -r requirements.txt
```

With standard Python:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Environment variables

Copy:

```bash
cp .env.example .env
```

Never commit `.env`.

The curriculum is provider-agnostic. Add only the API keys you actually use.

## Run tests

```bash
pytest -q
```

## Run the example API

```bash
uvicorn examples.production_api.main:app --reload
```

Then open `/docs` in your browser.
