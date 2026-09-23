.PHONY: install test serve docker

install:
	python -m pip install -r requirements.txt

test:
	pytest -q

serve:
	uvicorn examples.production_api.main:app --reload

docker:
	docker build -t modern-ai-engineering-path .
