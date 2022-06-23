install:
	pip install poetry
	pip install --upgrade poetry
	poetry install -v

test:
	poetry run pytest django-project -vv -s

coverage:
	poetry run pytest --cov=django-project --cov-report xml

missing-test:
	poetry run pytest --cov=django-project --cov-report term-missing

lint:
	poetry run flake8 django-project
	
package-install:
	make build
	pip install --user dist/*.whl

deps-export:
	poetry export -f requirements.txt --output requirements.txt

.PHONY: install test lint

