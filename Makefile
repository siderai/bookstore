install:
	pip install -r requirements.txt

test:
	pytest django-project -vv -s

coverage:
	pytest --cov=django-project --cov-report xml

missing-test:
	pytest --cov=django-project --cov-report term-missing

lint:
	flake8 django-project
