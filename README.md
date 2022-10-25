# Cookiecutter Template - PyPI Project

This is a [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template to create
a [Poetry](https://python-poetry.org/)-based Python project to be distributed at [PyPI](https://pypi.org/).
The project structure follows the pattern from the [apologies](https://github.com/pronovic/apologies)
demonstration project, using my [run-script-framework](https://github.com/pronovic/run-script-framework) and
shared GitHub Actions workflows from [gha-shared-workflows](https://github.com/pronovic/gha-shared-workflows).

To use it, first install cookiecutter:

```
pip install cookiecutter
```

Then, generate a new directory using the template:

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

> _Note:_ The `black_target`, `gha_matrix_os`, and `gha_matrix_python` fields are all comma-separated lists and must be quoted as shown.

The input above results in a directory called `sample-project`.  Make it
into a Git repository:

```
git init . && git add . && git commit -m "Initial revision based on pronovic/cookiecutter-pypi"
```

After that, follow the instructions in `DEVELOPER.md` to start working with
the repository.  Start with:

```
run install && run suite
```

Use `run --help` for more information.
