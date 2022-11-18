<h3 align="center">
  <img src="img/unstructured_logo.png" height="200">
</h3>

<h3 align="center">
  <p>Pre-Processing Pipeline for Nothing in Particular</p>
</h3>


The description for the pipeline repository goes here.
The API is hosted at `https://api.unstructured.io`.

### TODO list after generating repo from cookiecutter template:

- [ ] `git init`
- [ ] Update the pipeline name and description in `README.md` (this file)
- [ ] Add any additional requirements you need to `requirements/base.in` and run `make pip-compile`
- [ ] Run `make install`
- [ ] If needed, install additional dependencies in the `Dockerfile`
- [ ] Create an example notebook in `pipeline-notebooks` that demonstrates pre-processing of a specific data type
- [ ] Design an API with the notebook by using the special `pipeline-api` cell comments and function definition
- [ ] Generate the API with `make generate-api`
- [ ] Update `README.md` (this file) with examples of using the API and python code.
- [ ] Add tests in `test_{{ cookiecutter.pipeline_package }}`
- [ ] Delete this checklist and commit changes

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
  'http://localhost:8000/pipeline-{{ cookiecutter.pipeline_family }}/v0.0.0/change-to-real-route' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@example.pdf' \
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
| [Unstructured Community Github](https://github.com/Unstructured-IO/community) | Information about Unstructured.io community projects  |
| [Unstructured Github](https://github.com/Unstructured-IO) | Unstructured.io open source repositories |
| [Company Website](https://unstructured.io) | Unstructured.io product and company info |
