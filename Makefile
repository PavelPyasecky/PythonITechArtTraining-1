## Format your code using black
.PHONY: black
black:
	python -m black --version
	python -m black .

## Format imports in your code using isort
.PHONY: isort
isort:
	python -m isort --version
	python -m isort .

## Run tests using pytest
.PHONY: test
test:
	python -m pytest --version
	python -m pytest tests

## Lint your code using pylint
.PHONY: lint
lint:
	python -m pylint --version
	python -m pylint app

## Run ci part
.PHONY: ci
ci:
	pre-commit run black
	pre-commit run isort
	pre-commit run test
