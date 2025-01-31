# Cookiecutter Template - PyPI Project

This is a [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template to create a Python project to be distributed at [PyPI](https://pypi.org/).  It includes integration with [GitHub Actions](https://docs.github.com/en/actions), [readthedocs.io](https://readthedocs.org/) and [coveralls.io](https://coveralls.io/).

The project structure follows the pattern from the [apologies](https://github.com/pronovic/apologies) demonstration project.  [Poetry](https://python-poetry.org/) is used manage Python packaging and dependencies, and most day-to-day tasks (such as running unit tests from the command line) are orchestrated through Poetry using my [run-script-framework](https://github.com/pronovic/run-script-framework).  A coding standard is enforced using [Black](https://pypi.org/project/black/), [isort](https://pypi.org/project/isort/) and [Pylint](https://pypi.org/project/pylint/).  Python 3 type hinting is validated using [MyPy](https://pypi.org/project/mypy/).  The GitHub Actions workflow is a matrix build implemented using my [gha-shared-workflows](https://github.com/pronovic/gha-shared-workflows).  There are also pre-commit hooks to enforce the code style checks.  A generated `DEVELOPER.md` file provides notes about how the code is structured, how to set up a development environment, etc.

## Prerequisites

To use this template, you need to install [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/):

```
pipx install cookiecutter
```

The resulting project depends on the [Poetry](https://python-poetry.org/) build tool.  You need to install only a Python 3 interpreter and Poetry.  Poetry itself takes care of everything else.  See the [instructions](POETRY.md).

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
project_slug [sample-project]:
project_name [Sample Project]:
short_description [Short description]:
author_name [First Last]:
author_email [first.last@example.com]:
github_owner [owner]:
github_repo [samplerepo]:
default_branch [main]:
package [sample]:
python_version [>=3.9,<4]:
black_target [py39 py310]:
copyright_year [2022]:
```

The project slug is the name of the resulting directory, so in this example the project will be generated in `sample-project`:

```
cd sample-project
```

Then, initialize the Git repository:

```
git init . && git add . && git commit -m "Initial revision based on pronovic/cookiecutter-pypi"
```

Assuming you have already installed `poetry` (per the [instructions](POETRY.md)), you can get things started using the `run` script.  First, install the dependencies and set up the pre-commit hooks:

```
./run install 
```

Finally, run the test suite:

```
./run suite
```

Assuming the test suite passes, you'll have to check in `poetry.lock` with the current version of all dependencies:

```
git add poetry.lock && git commit -m "Add initial poetry.lock" poetry.lock
```

Then, you can push to your repository and test the GitHub Actions process.

> _Note:_ To see what other commands are available, use `./run --help`.  See the generated `DEVELOPER.md` file for more information about the development environment, including integration with [PyCharm](https://www.jetbrains.com/pycharm/download), etc.

You will need to manually adjust `.github/workflows/test-suite.yml` to reflect the platforms and Python versions that you want to test.  The suggested workflow runs a matrix build on Linux for all supported Python versions, and a build on Windows and MacOS only for the latest Python version.  In GitHub Actions, the Linux runners are _much_ faster and more reliable, so this strategy seems to yield the best results.
