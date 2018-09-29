PYTHON = python3.6
PIP = pip
ISORT = isort
ISORT_ARGS = -rc src/zveronics tests

all:

venv:
	$(PYTHON) -m virtualenv venv

.PHONY: install
install:
	$(PIP) install .

,PHONY: develop
develop:
	$(PIP) install -e .

.PHONY: check
check: check-linters check-coverage

.PHONY: check-linters
check-linters: check-isort check-pylint

.PHONY: check-isort
check-isort:
	$(ISORT) --diff $(ISORT_ARGS)

.PHONY: check-pylint
format-isort:
	$(PYLINT) zveronics

.PHONY: format-isort
format-isort:
	$(ISORT) -y $(ISORT_ARGS)
