# Cookiecutter Template - PyPI Project

This is a [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template to create a Python project to be distributed at [PyPI](https://pypi.org/).  It includes integration with [GitHub Actions](https://docs.github.com/en/actions), [readthedocs.io](https://readthedocs.org/) and [coveralls.io](https://coveralls.io/).

The project structure follows the pattern from the [apologies](https://github.com/pronovic/apologies) demonstration project.  [Poetry](https://python-poetry.org/) is used manage Python packaging and dependencies, and most day-to-day tasks (such as running unit tests from the command line) are orchestrated through Poetry using my [run-script-framework](https://github.com/pronovic/run-script-framework).  A coding standard is enforced using [Black](https://pypi.org/project/black/), [isort](https://pypi.org/project/isort/) and [Pylint](https://pypi.org/project/pylint/).  Python 3 type hinting is validated using [MyPy](https://pypi.org/project/mypy/).  The GitHub Actions workflow is a matrix build implemented using my [gha-shared-workflows](https://github.com/pronovic/gha-shared-workflows).  There are also pre-commit hooks to enforce the code style checks.  A generated `DEVELOPER.md` file provides notes about how the code is structured, how to set up a development environment, etc.

## Prerequisites

To use this template, you need to install [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/):

```
pip install cookiecutter
```

The resulting project depends on the [Poetry](https://python-poetry.org/) build tool.  You need to install only a Python 3 interpreter and Poetry.  Poetry itself takes care of everything else.  See the [instructions](POETRY.md).

The developer process described in the resulting `DEVELOPER.md` file assumes you are working a UNIX-style shell, such as bash. On Windows, you are expected to be using the Git bash emulator installed with [Git for Windows](https://gitforwindows.org/).

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
copyright_year [2022]:
```

> _Note:_ You will need to manually adjust `.github/workflows/test-suite.yml` to reflect the platforms and Python versions that you want to test.  The suggested workflow runs a matrix build on Linux for all supported Python versions, and a build on Windows and MacOS only for the latest Python version.  In GitHub Actions, the Linux runners are _much_ faster and more reliable, so this strategy seems to yield the best results.

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

Use `./run --help` to list available commands.  See the generated `DEVELOPER.md` file for more information about the development environment, including integration with [PyCharm](https://www.jetbrains.com/pycharm/download), etc.
