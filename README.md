# Cookiecutter Template - PyPI Project

This is a [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template to create a Python project to be distributed at [PyPI](https://pypi.org/).  It includes integration with [GitHub Actions](https://docs.github.com/en/actions), [readthedocs.io](https://readthedocs.org/) and [coveralls.io](https://coveralls.io/).

The project structure follows the pattern from the [apologies](https://github.com/pronovic/apologies) demonstration project.  [UV](https://docs.astral.sh/uv/) is used manage Python packaging and dependencies, and most day-to-day tasks (such as running unit tests from the command line) are orchestrated through UV using my [run-script-framework](https://github.com/pronovic/run-script-framework).  A coding standard is enforced using [Ruff](https://pypi.org/project/ruff/).  Python 3 type hinting is validated using [MyPy](https://pypi.org/project/mypy/).  The GitHub Actions workflow is a matrix build implemented using my [gha-shared-workflows](https://github.com/pronovic/gha-shared-workflows).  There are also pre-commit hooks to enforce the code style checks.  A generated `DEVELOPER.md` file provides notes about how the code is structured, how to set up a development environment, etc.

## Prerequisites

To use this template, you need to install [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/):

```
pipx install cookiecutter
```

The resulting project depends on the [UV](https://docs.astral.sh/uv/) build tool.  All you need to do install UV itself, following the [instructions](https://docs.astral.sh/uv/getting-started/installation/).  UV will take care of installing the required Python interpreter and all of the dependencies.

The developer process described in the resulting `DEVELOPER.md` file assumes you are working a UNIX-style shell, such as bash. On Windows, you are expected to be using the Git bash emulator installed with [Git for Windows](https://gitforwindows.org/).

## Release Process

By default, the release process in the generated `.github/workflows/test-suite.yml` workflow is configured to publish artifacts by attaching them to a release in the GitHub repository. (The generated `DEVELOPER.md` file contains instructions.)  Optionally, you can also publish to PyPI.  To do this, create an account at PyPI for yourself, and register your project.  Once the project exists, go to your PyPI [account settings](https://pypi.org/manage/account/) and create an API token with upload permissions for the new project.  In your GitHub repository, add a GitHub Actions secret called `PYPI_TOKEN` to hold the token.  Then, adjust `test-suite.yml` to set `publish-pypi: true`.

## Instructions for Use

Use `cookiecutter` to execute the template:

```
cookiecutter gh:pronovic/cookiecutter-pypi
```

When prompted, provide values for all of the template parameters:

```
  [1/10] project_slug (sample-project):
  [2/10] project_name (Sample Project):
  [3/10] short_description (Short description):
  [4/10] author_name (First Last):
  [5/10] author_email (first.last@example.com):
  [6/10] github_owner (owner):
  [7/10] github_repo (samplerepo):
  [8/10] default_branch (main):
  [9/10] package (sample):
  [10/10] copyright_year (2025):
```

The project slug is the name of the resulting directory, so in this example the project will be generated in `sample-project`:

```
cd sample-project
```

Then, initialize the Git repository:

```
git init . && git add . && git commit -m "Initial revision based on pronovic/cookiecutter-pypi"
```

Assuming you have already installed `uv` (per the [instructions](https://docs.astral.sh/uv/getting-started/installation/)), you can get things started using the `run` script.  First, install the dependencies and set up the pre-commit hooks:

```
uv lock && ./run install 
```

Finally, run the test suite:

```
./run suite
```

Assuming the test suite passes, you'll have to check in `uv.lock` with the current version of all dependencies:

```
git add uv.lock && git commit -m "Add initial uv.lock" uv.lock
```

Then, you can push to your repository and test the GitHub Actions process.

> **Note:** you may need to manually adjust `pyproject.toml` to properly reflect your URLs and the metadata you want to publish.

## Development Process

See the generated `DEVELOPER.md` file for more information about the development environment, including integration with [PyCharm](https://www.jetbrains.com/pycharm/download), etc.

The generated `run` script is the entry point for developers and for the GitHub Actions CI/CD process.  It wraps `uv` and other build tools to standardize various common tasks.  To see what other commands are available, use `./run --help`.

## Python Version

My general policy is to support the most recent four versions of the Python interpreter, and the template is designed around this assumption.

For example, starting in late 2025, I dropped support for Python 3.10, leaving support for Python 3.11, 3.12, 3.13, and 3.14.  I think that this represents a decent compromise between broad applicability &mdash; making the package available to as many users as possible &mdash; and the non-zero overhead of supporting each additional version.  These days Python is released about once per year, so most people should be able to run one of the supported versions, even on a long-term support Linux distribution.  Every year, I update the template at approximately the same time I update my packages to support the latest version of Python.

Whenever you want to change the set of supported versions in your own package, you need to adjust the following files:

- `.python-version`
- `.readthedocs.yaml`
- `pyproject.toml`
- `.github/workflows/test-suite.yml`

For local testing, `run install` will use the version in `.python-version` by default.  If you want to test with a different version, export that version in your shell (i.e. `export UV_PYTHON=3.14`) and execute `run install` again.  This will rebuild the virtualenv to use the new interpreter.  Don't forget to `unset UV_PYTHON` and rebuild the virtualenv when you're done testing.
