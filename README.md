# Cookiecutter Template - PyPI Project

This is a [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template to create a Python project to be distributed at [PyPI](https://pypi.org/).  It includes integration with [GitHub Actions](https://docs.github.com/en/actions), [readthedocs.io](https://readthedocs.org/) and [coveralls.io](https://coveralls.io/).

The project structure follows the pattern from the [apologies](https://github.com/pronovic/apologies) demonstration project.  [Poetry](https://python-poetry.org/) is used manage Python packaging and dependencies, and most day-to-day tasks (such as running unit tests from the command line) are orchestrated through Poetry using my [run-script-framework](https://github.com/pronovic/run-script-framework).  A coding standard is enforced using [Black](https://github.com/psf/black), [isort](https://pypi.org/project/isort/) and [Pylint](https://www.pylint.org/).  Python 3 type hinting is validated using [MyPy](https://pypi.org/project/mypy/).  The GitHub Actions workflow is a matrix build implemented using my [gha-shared-workflows](https://github.com/pronovic/gha-shared-workflows).  There are also pre-commit hooks to enforce the code style checks.  A generated `DEVELOPER.md` file provides notes about how the code is structured, how to set up a development environment, etc.

## Prerequisites

To use this template, you need to install [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/):

```
pip install cookiecutter
```

The resulting project depends on the [Poetry](https://python-poetry.org/) build tool.  You need to install only a Python 3 interpreter and Poetry.  Poetry itself takes care of everything else.  See the [instructions](POETRY.md).

## Instructions for Use

Use `cookiecutter` to execute the template:

```
cookiecutter gh:pronovic/cookiecutter-pypi
```

When prompted, provide values for all of the template parameters:

```
project_slug [sample-project]:
project_name [Sample Project]:
short_description [Short description]:
author_name [First Last]:
author_email [first.last@example.com]:
github_owner [owner]:
github_repo [samplerepo]:
default_branch [master]:
package [sample]:
python_version [>=3.9,<4]:
black_target ['py39', 'py310']:
gha_matrix_os ['ubuntu-latest', 'macos-latest', 'windows-latest']:
gha_matrix_python ['3.9', '3.10']:
copyright_year [2022]:
```

> _Note:_ The `black_target`, `gha_matrix_os`, and `gha_matrix_python` fields are all comma-separated lists and must be quoted as shown.  The `black_target` is substituted into `pyproject.toml` and the `gha_` values are substituted into the matrix build for the GitHub Actions build in `.github/workflows/test-suite.yml`.  Start with the defaults unless you have a reason to change them.

The project slug is the name of the resulting directory, so in this example the project will be generated in `sample-project`.  Change to that directory, and initialize a Git repository:

```
git init . && git add . && git commit -m "Initial revision based on pronovic/cookiecutter-pypi"
```

After that, follow the instructions in the resulting `DEVELOPER.md` file to work with the repository.  Assuming you have already installed `poetry` (per the [instructions](POETRY.md)), you can get things started using the `run` script:

```
run install && run suite
```

Use `run --help` for more information about the available tasks.
