PIP_VERSION := 22.1.2

.PHONY: help
help: Makefile
	@sed -n 's/^\(## \)\([a-zA-Z]\)/\2/p' $<


###########
# Install #
###########

.PHONY: install-base
install-base: install-base-pip-packages

## install:                     installs all test and dev requirements
.PHONY: install
install: install-base

.PHONY: install-base-pip-packages
install-base-pip-packages:
	python3 -m pip install pip==${PIP_VERSION}
	pip install -r requirements/base.txt

## pip-compile:                 compiles all base/dev/test requirements
.PHONY: pip-compile
pip-compile:
	pip-compile requirements/base.in

#########
# Build #
#########

## generate-repo:               generates pipeline repo from template
.PHONY: generate-repo
generate-repo:
	cookiecutter .
	