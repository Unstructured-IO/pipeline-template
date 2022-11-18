<h3 align="center">
  <img src="img/unstructured_logo.png" height="200">
</h3>

<h3 align="center">
  <p>Pre-Processing Pipeline Template</p>
</h3>


The description for the pipeline repository goes here.
The API is hosted at `https://api.unstructured.io`.

### Updates TODO list

- [ ] Update the pipeline name and description in `README.md` (this file)
- [ ] Rename all instances of {{ cookiecutter.pipeline_family }} in `README.md` (this file)
- [ ] Update the pipeline family name and pipeline package in the `Makefile`
- [ ] Update the pipeline name in `preprocessing-pipeline-family.yaml`
- [ ] Rename the folders `prepline_template` and `test_template`
- [ ] Change name of the variable `PIPELINE_FAMILY` at the top of `.github/workflows/ci.yml`
- [ ] If needed, install additional dependencies in the `Dockerfile`
- [ ] Add any additional requirements you need to `requirements/base.in` and run `make pip-compile`

## Developer Quick Start

* Using `pyenv` to manage virtualenv's is recommended
	* Mac install instructions. See [here](https://github.com/Unstructured-IO/community#mac--homebrew) for more detailed instructions.
		* `brew install pyenv-virtualenv`
	  * `pyenv install 3.8.13`
  * Linux instructions are available [here](https://github.com/Unstructured-IO/community#linux).

  * Create a virtualenv to work in and activate it, e.g. for one named `{{ cookiecutter.pipeline_family }}`:

	`pyenv  virtualenv 3.8.13 {{ cookiecutter.pipeline_family }}` <br />
	`pyenv activate {{ cookiecutter.pipeline_family }}`

* Run `make install`
* Start a local jupyter notebook server with `make run-jupyter` <br />
	**OR** <br />
	just start the fast-API locally with `make run-web-app`

#### Extracting whatever from some type of document

Give a description of making API calls using example `curl` commands, and example JSON responses.

For example:
```
curl -X 'POST' \
  'http://localhost:8000/pipeline-{{ cookiecutter.pipeline_family }}/v0.0.0/blahblah' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@rgld-10-K-85535-000155837021011343.xbrl' \
  -F 'some_parameter=something'  | jq -C . | less -R
```

It's also nice to show how to call the API function using pure Python.

### Generating Python files from the pipeline notebooks

You can generate the FastAPI APIs from your pipeline notebooks by running `make generate-api`.

## Security Policy

See our [security policy](https://github.com/Unstructured-IO/pipeline-{{ cookiecutter.pipeline_family }}/security/policy) for
information on how to report security vulnerabilities.

## Learn more

| Section | Description |
|-|-|
| [Company Website](https://unstructured.io) | Unstructured.io product and company info |
