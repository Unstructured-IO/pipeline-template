<h3 align="center">
  <img src="{{ cookiecutter.repo_name }}/img/unstructured_logo.png" height="200">
</h3>

&nbsp;

# Cookiecutter Template for Pipeline Family Repositories

This repository serves as a template for creating pipeline family repositories. It makes use of
[`cookiecutter`](https://github.com/cookiecutter/cookiecutter) to make the process as quick and
easy as possible.

To be clear, this is not a pipeline family repository, it is a tool for creating pipeline family
repositories.

## Getting Started

1. Initiating repo generation:
    1. Generating a repo from this template without cloning this repo:

        This repo need not be cloned to use its template functionality. To generate a new repo from template:
        1. Make sure `cookiecutter` is installed in your current environment (`pip install cookiecutter` will install it)
        1. Run `cookiecutter git@github.com:Unstructured-IO/pipeline-template.git`

    1. Generating a repo from this template after cloning this repo:

        From the base directory of the cloned repo:
        1. Run `make install`
        2. Run `make generate-repo`
1. Provide input for the different template fields
1. Open `README.md` in the base folder of the generated repo and work through the checklist
