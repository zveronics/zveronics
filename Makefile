PYTHON3    = python3.6
PYTHON     = python
PIP        = pip
PYLINT     = pylint
FLAKE8     = flake8
COVERAGE   = coverage
ISORT      = isort
ISORT_ARGS = -rc src/zveronics tests

all:

venv:
	$(PYTHON3) -m virtualenv venv

.PHONY: install
install:
	$(PYTHON) install .

,PHONY: develop
develop:
	$(PIP) install -e .

.PHONY: check-all
check-all: check-linters check-coverage

.PHONY: check-linters
check-linters: check-isort check-pylint check-flake8

.PHONY: check-isort
check-isort:
	$(ISORT) --diff $(ISORT_ARGS)

.PHONY: check-pylint
check-pylint:
	$(PYLINT) zveronics

.PHONY: check-flake8
check-flake8:
	$(FLAKE8) src/zveronics

.PHONY: check-coverage
check-coverage: coverage-report

.PHONY: coverage-run
coverage-run:
	$(COVERAGE) run -m pytest

.PHONY: format
format: format-isort

.PHONY: format-isort
format-isort:
	$(ISORT) -y $(ISORT_ARGS)

.PHONY: coverage-report
coverage-report: coverage-run
	$(COVERAGE) report
