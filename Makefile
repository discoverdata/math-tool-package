run:
	python main.py
test:
	pytest tests/

lint:
	flake8 src

install:
	pip install --editable . --use-pep517
