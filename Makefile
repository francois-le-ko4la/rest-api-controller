# Makefile

PACKAGE_NAME = rest-api-controller
MAKE := $(MAKE) --no-print-directory
SHELL = bash

default:
	@echo "Makefile for $(PACKAGE_NAME)"
	@echo
	@echo 'Usage:'
	@echo
	@echo '    make install    install the packages' 
	@echo '    make clean      remove the package'
	@echo '    make test       test'
	@echo

install:
	@./setup.py install

clean:
	@rm -Rf *.egg *.egg-info .cache .coverage .tox build dist docs/build htmlcov
	@find -depth -type d -name __pycache__ -exec rm -Rf {} \;
	@find -type f -name '*.pyc' -delete

test:
	@./setup.py test

.PHONY: default install clean test
